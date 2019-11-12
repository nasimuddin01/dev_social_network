# Generated by Django 2.2.6 on 2019-11-12 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=5)),
                ('status', models.CharField(choices=[('M', 'Married'), ('S', 'Single')], default=1, max_length=10)),
                ('website', models.URLField(max_length=283)),
                ('company', models.CharField(max_length=120)),
                ('profession', models.CharField(choices=[('S/L', 'Student or Learning'), ('JD', 'Junior Developer'), ('SD', 'Senior Developer'), ('D', 'Developer'), ('M', 'Manager'), ('I/T', 'Instructor or Teacher'), ('I', 'Intern'), ('B', 'Bussiness Man'), ('DM', 'Digital Marketer'), ('DS', 'Data Scientist'), ('O', 'Other')], default='Web Developer', max_length=120)),
                ('location', models.CharField(default='USA', max_length=100)),
                ('skills', models.CharField(max_length=120)),
                ('bio', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='profiles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]