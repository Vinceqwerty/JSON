import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message


# CREATE
@csrf_exempt
def create_message(request):
    if request.method == "POST":
        data = json.loads(request.body)

        message = Message.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            content=data.get("content")
        )

        return JsonResponse({
            "status": "success",
            "id": message.id,
            "message": "Message saved successfully"
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


# READ ALL
def get_messages(request):
    if request.method == "GET":
        messages = list(Message.objects.values())

        return JsonResponse({
            "status": "success",
            "data": messages
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


# READ SINGLE
def get_message(request, id):
    if request.method == "GET":
        try:
            message = Message.objects.get(id=id)

            return JsonResponse({
                "status": "success",
                "data": {
                    "id": message.id,
                    "name": message.name,
                    "email": message.email,
                    "content": message.content
                }
            })

        except Message.DoesNotExist:
            return JsonResponse({"error": "Message not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)


# UPDATE
@csrf_exempt
def update_message(request, id):
    if request.method == "PUT":
        try:
            message = Message.objects.get(id=id)
            data = json.loads(request.body)

            message.name = data.get("name", message.name)
            message.email = data.get("email", message.email)
            message.content = data.get("content", message.content)

            message.save()

            return JsonResponse({
                "status": "success",
                "message": "Message updated successfully"
            })

        except Message.DoesNotExist:
            return JsonResponse({"error": "Message not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)


# DELETE
@csrf_exempt
def delete_message(request, id):
    if request.method == "DELETE":
        try:
            message = Message.objects.get(id=id)
            message.delete()

            return JsonResponse({
                "status": "success",
                "message": "Message deleted successfully"
            })

        except Message.DoesNotExist:
            return JsonResponse({"error": "Message not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)
