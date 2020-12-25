from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from linkedin_v2 import linkedin
from django.conf import settings

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")

def linked_in_login(request):
    authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,
                                                              USER_TOKEN, USER_SECRET,
                                                              RETURN_URL, linkedin.PERMISSIONS.enums.values())

    # Pass it in to the app...

    application = linkedin.LinkedInApplication(authentication)

    # Use the app....

    application.get_profile()

    return render(request, "linkedinloginpage.html", {
        "application_profile": application.get_profile()
    })

