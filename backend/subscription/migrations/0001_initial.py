# Generated by Django 5.2.3 on 2025-07-02 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionBox',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('frequency', models.CharField(choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('Twice a week', 'Twice a week')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledItem',
            fields=[
                ('scheduled_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(choices=[('kg', 'Kg'), ('bunch', 'Bunch')], max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_items', to='subscription.subscriptionbox')),
            ],
        ),
    ]
