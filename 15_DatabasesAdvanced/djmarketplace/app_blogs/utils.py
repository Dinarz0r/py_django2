from app_blogs.models import Profile


def up_points(user_id, points):
    profile = Profile.objects.filter(user_id=user_id).first()
    profile.points_status += points
    profile.save(update_fields=['points_status'])


def down_points(user_id, points):
    profile = Profile.objects.filter(user_id=user_id).first()
    profile.points_status -= points
    profile.save(update_fields=['points_status'])


def assign_a_status(user_id):
    profile = Profile.objects.filter(user_id=user_id).first()
    if profile.points_status < 1000:
        profile.verification = 'newbie'
    elif 1000 <= profile.points_status <= 10000:
        profile.verification = 'Advanced'
    elif 10000 < profile.points_status:
        profile.verification = 'Expert'
    profile.save(update_fields=['verification'])
