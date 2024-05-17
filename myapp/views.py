
from django.core.paginator import Paginator
from . models import Event,Events1,Booking,EventDetail,Feedback
from .forms import BookingForm,FeedbackForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def delete_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        booking.delete()
        return redirect('my_events')
    else:
        return redirect('index')  # Redirect to homepage if accessed via GET request
def index(request):
    return render(request,'index.html')
def about(request):
    # Fetch all events
    events = Event.objects.all()

    # Configure number of items per page
    items_per_page = 5

    # Paginate the events
    paginator = Paginator(events, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'about.html', {'page_obj': page_obj})


def events1(request):
    if request.user.is_authenticated:
        return redirect('events')  # Redirect to events page if user is logged in
    else:
        events1 = Events1.objects.all()
        return render(request, 'events1.html', {'events1': events1})


def event_list(request):
    events = Events1.objects.all()
    return render(request, 'feedback_success.html', {'events': events})



@login_required
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)



def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.user = request.user
            booking_instance.save()

            # Send email notification
            subject = 'Event Booking Confirmation'
            context = {
                'user': request.user,
                'event': booking_instance.event_name,
                'date': booking_instance.booking_date,
            }
            html_message = render_to_string('booking_confirmation_email.html', context)
            plain_message = strip_tags(html_message)
            send_mail(
                subject,
                plain_message,
                'ashnaashna12718.com',  # Sender's email address
                [request.user.email],  # Recipient's email address (assuming user's email is stored in request.user.email)
                html_message=html_message,
            )

            return redirect('thanks')
    else:
        form = BookingForm()

    events = Event.objects.all()  # Fetch all events from the database
    context = {
        'form': form,
        'events': events,  # Pass the events to the template context
    }
    return render(request, 'booking.html', context)


@login_required
def my_events(request):
    # Filter the booked events queryset based on the currently logged-in user
    booked_events = Booking.objects.filter(user=request.user)
    return render(request, 'my_events.html', {'booked_events': booked_events})

def thanks_view(request):
    return render(request, 'thanks.html')

def contact(request):
    return render(request,'contact.html')


def booking_confirmation_email(request):
    subject = 'Booking Confirmation'
    user = request.user  # Assuming user is logged in
    event = ...  # Get the event object for which the booking confirmation is being sent

    context = {
        'user': user,
        'event': event,
    }

    html_message = render_to_string('booking_confirmation_email.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        'your_email@example.com',  # Sender's email address
        [user.email],  # Recipient's email address (assuming user's email is stored in request.user.email)
        html_message=html_message,
    )

    return render(request,
                  'booking_confirmation_sent.html')
    # Optional: render a page confirming that the email has been sent
def update_booking(request, booking_id):
    # Retrieve the booking object
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        # Create a form instance with the updated data
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            # Save the updated booking
            updated_booking = form.save()

            # Send email notification to the customer
            subject = 'Booking Updated'
            context = {
                'user': request.user,
                'event': updated_booking.event_name,
                'booking_date': updated_booking.booking_date,  # Include booking_date in context
                # Add more context variables as needed
            }
            html_message = render_to_string('booking_update_confirmation_email.html', context)
            plain_message = strip_tags(html_message)
            send_mail(
                subject,
                plain_message,
                'your_email@example.com',  # Sender's email address
                [updated_booking.cus_email],  # Recipient's email address
                html_message=html_message,
            )

            return redirect('my_events')  # Redirect to my_events page after updating
    else:
        # Create a form instance with the existing booking data
        form = BookingForm(instance=booking)

    return render(request, 'update_booking.html', {'form': form})
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event_detail = EventDetail.objects.get(event=event)  # Retrieve the EventDetail object related to the Event
    return render(request, 'event_detail.html', {'event': event, 'event_detail': event_detail})


@login_required
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.created_by = request.user
            feedback.save()
            return redirect('/')  # Redirect to the home page after successful form submission
    else:
        form = FeedbackForm()

    # Get the feedbacks created by the logged-in user
    user_feedbacks = Feedback.objects.filter(created_by=request.user)

    return render(request, 'feedback.html', {'form': form, 'user_feedbacks': user_feedbacks})

def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST' and request.user == feedback.created_by:
        feedback.delete()
    return redirect('feedback')

def feedback1(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback1.html', {'feedbacks': feedbacks})

