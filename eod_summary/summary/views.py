from django.shortcuts import render
from openai import OpenAI
from dotenv import load_dotenv
from django.http import HttpResponse, JsonResponse

load_dotenv()

import os
from supabase import create_client, Client

url: str = os.environ.get("supabase_url")
key: str = os.environ.get("supabase_key")
print(url, "\n", key)
supabase: Client = create_client(url, key)
print(supabase, "connected to supabase!!")

# Create your views here.
client = OpenAI(api_key="")


def hello(request):
    return HttpResponse("Hello, world!")


def pull_records(request):
    try:  # gte stands for "greater than or equal to", and lte stands for "less than or equal to".
        response = (
            supabase.table("books")
            .select("name", "price")
            .filter("id", "gte", 101)
            .filter("id", "lte", 111)
            .execute()
        )
        data = response.data
        summary = summarize(data)
        return JsonResponse({"summary": summary}, safe=False)
        # return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def summarize(content):
    try:
        print(content)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes book reading data.",
                },
                {
                    "role": "user",
                    "content": f"I have read the following books: {content}. Can you summarize this information?",
                },
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"