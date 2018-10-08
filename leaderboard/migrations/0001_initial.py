# Generated by Django 2.0.8 on 2018-10-07 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Game_Name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Player_Name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_Name', models.CharField(max_length=32)),
                ('Player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player1', to='leaderboard.Player')),
                ('Player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player2', to='leaderboard.Player')),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Team'),
        ),
        migrations.AddField(
            model_name='result',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='leaderboard.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='leaderboard.Team'),
        ),
    ]
