# Generated by Django 2.2.4 on 2019-08-22 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import sms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount_to_pay', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='GradeScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=100, unique=True)),
                ('mark_from', models.IntegerField(unique=True)),
                ('mark_upto', models.IntegerField(unique=True)),
                ('remark', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('current_session', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_logo', models.ImageField(blank=True, null=True, upload_to='pictures/')),
                ('school_address', models.CharField(blank=True, max_length=300, null=True)),
                ('school_town', models.CharField(blank=True, max_length=100, null=True)),
                ('school_slogan', models.CharField(blank=True, max_length=200, null=True)),
                ('business_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('business_phone1', models.CharField(blank=True, max_length=11, null=True)),
                ('business_phone2', models.CharField(blank=True, max_length=11, null=True)),
                ('social_link1', models.CharField(blank=True, max_length=200, null=True)),
                ('social_link2', models.CharField(blank=True, max_length=200, null=True)),
                ('social_link3', models.CharField(blank=True, max_length=200, null=True)),
                ('ft_begins', models.DateField(blank=True, null=True)),
                ('ft_ends', models.DateField(blank=True, null=True)),
                ('st_begins', models.DateField(blank=True, null=True)),
                ('st_ends', models.DateField(blank=True, null=True)),
                ('tt_begins', models.DateField(blank=True, null=True)),
                ('tt_ends', models.DateField(blank=True, null=True)),
                ('sms_unit', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_user', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('date_send', models.DateTimeField(auto_now_add=True)),
                ('body', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=7)),
                ('clss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Class')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Session')),
                ('subjects', models.ManyToManyField(blank=True, to='sms.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_admission', models.CharField(blank=True, max_length=100, null=True)),
                ('roll_number', models.CharField(max_length=50)),
                ('in_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Class')),
                ('session', models.ForeignKey(default=sms.models.get_current_session, on_delete=django.db.models.deletion.CASCADE, to='sms.Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SectionAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeholder', models.CharField(max_length=100)),
                ('signature', models.ImageField(blank=True, null=True, upload_to='school_signature/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Section')),
                ('section_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=12)),
                ('cumulative', models.FloatField()),
                ('rank', models.CharField(blank=True, max_length=5, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_amount', models.FloatField()),
                ('due_amount', models.FloatField()),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Cheaque', 'Cheaque')], max_length=50)),
                ('payment_status', models.CharField(choices=[('Paid', 'Fully Paid'), ('Not Paid', 'Not Paid'), ('Partially Paid', 'Partially Paid')], max_length=50)),
                ('term', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=7)),
                ('teller_number', models.CharField(blank=True, max_length=100, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='sms.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=300)),
                ('unread', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('message_type', models.CharField(choices=[('Success', 'Success'), ('Error', 'Error'), ('Info', 'Info')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(blank=True, max_length=100, null=True)),
                ('post_body', models.TextField(blank=True, null=True)),
                ('posted_to', models.CharField(blank=True, max_length=100, null=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=7)),
                ('fca', models.CharField(max_length=10)),
                ('sca', models.CharField(max_length=10)),
                ('exam', models.CharField(max_length=10)),
                ('total', models.FloatField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=1, null=True)),
                ('remark', models.CharField(blank=True, max_length=50, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='FeeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('term', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=7)),
                ('for_class', models.ManyToManyField(to='sms.Class')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Session')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('term', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=7)),
                ('amount', models.FloatField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Session')),
            ],
        ),
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='articles_pictures/%Y/%m/%d/', verbose_name='Featured image')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=80, null=True)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('S', 'Delivered'), ('P', 'Pending')], default='P', max_length=1)),
                ('content', markdownx.models.MarkdownxField()),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('recipients', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mail',
                'verbose_name_plural': 'Mails',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.AddField(
            model_name='class',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Section'),
        ),
        migrations.AddField(
            model_name='class',
            name='subjects',
            field=models.ManyToManyField(to='sms.Subject'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=7)),
                ('date', models.DateField()),
                ('is_present', models.BooleanField(default=False)),
                ('is_late', models.BooleanField(blank=True, null=True)),
                ('is_late_for', models.CharField(blank=True, max_length=4, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Student')),
            ],
        ),
    ]