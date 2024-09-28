from .modules import *


# Create your views here.


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_multiple_images(request):
    images = request.FILES.getlist('images')  # Get multiple files from the request
    image_names = request.data.getlist('image_names', [])  # Optional: Names for images
    image_descriptions = request.data.getlist('image_descriptions', [])  # Optional: Descriptions for images

    if not images:
        return Response({'error': 'No images provided'}, status=status.HTTP_400_BAD_REQUEST)

    created_images = []

    # Iterate over the images and create ProductImage instances
    for idx, image in enumerate(images):
        image_name = image_names[idx] if len(image_names) > idx else None
        image_description = image_descriptions[idx] if len(image_descriptions) > idx else None

        # Create a new ProductImage instance
        product_image = ProductImage.objects.create(
            ImageUrl=image,
            ImageName=image_name,
            ImageDescription=image_description
        )
        created_images.append(product_image)

    # Serialize the created images and return them in the response
    serializer = ProductImageSerializer(created_images, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_all_images(request):
    try:
        images = ProductImage.objects.all()
        serializer = ProductImageSerializer(images, many=True,context={'request': request})
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Get All Images Fetched Successfully',
            'data': serializer.data
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })





# Render HTML template
def index(request):
    dict ={

    }
    return render(request, 'provider/invoice.html', dict)  # Rendering the invoice.html template


import requests
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from weasyprint import HTML
from io import BytesIO

# URL for your Node.js Order creation API
NODEJS_ORDER_API = "https://app.bestelectronics.com.bd/api/v1/order/orderCreate"


def create_order_and_send_invoice(request):
    if request.method == "POST":
        # Extract the order details from the request (from Django form or passed directly)
        order_data = {
            "customer": request.POST.get("customer"),
            "email": request.POST.get("email"),
            "orderType": request.POST.get("orderType"),
            "deliveryAddress": request.POST.get("deliveryAddress"),
            "userName": request.POST.get("userName"),
            "district": request.POST.get("district"),
            "phoneNumber": request.POST.get("phoneNumber"),
            "orderNote": request.POST.get("orderNote"),
            "firstName": request.POST.get("firstName"),
            "lastName": request.POST.get("lastName"),
            "channel": request.POST.get("channel"),
            "outlet": request.POST.get("outlet"),
            "customerIp": request.POST.get("customerIp"),
            "paymentMethod": request.POST.get("paymentMethod"),
            "products": request.POST.get("products"),
            "couponName": request.POST.get("couponName"),
        }

        # Make the API call to create the order
        response = requests.post(NODEJS_ORDER_API, json=order_data)

        if response.status_code == 200:
            order = response.json()["order"]["createdOrder"]["order"]

            # Render the invoice template with dynamic order data
            html_content = render_to_string("provider/invoice.html", {"order": order})

            # Generate PDF from HTML content using WeasyPrint
            pdf_file = BytesIO()
            HTML(string=html_content).write_pdf(pdf_file)
            pdf_file.seek(0)

            # Send the invoice PDF via email
            email_subject = f"Invoice for your order {order['orderId']}"
            email_body = "Please find the attached invoice for your recent order."
            email = EmailMessage(
                email_subject,
                email_body,
                "no-reply@bestelectronics.com.bd",  # From email
                [order["email"]],  # To email (customer email)
            )
            email.attach(f"Invoice-{order['orderId']}.pdf", pdf_file.read(), "application/pdf")
            email.send()

            return render(request, "provider/order_success.html", {"order": order})
        else:
            return render(request, "provider/order_failure.html", {"error": response.json()})



