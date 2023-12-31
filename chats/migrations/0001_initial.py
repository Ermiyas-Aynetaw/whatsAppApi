# Generated by Django 4.1.3 on 2023-12-01 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('max_members', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('chatroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chatroom')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.user')),
            ],
        ),
        migrations.AddField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(related_name='chatrooms', to='chats.user'),
        ),
    ]
