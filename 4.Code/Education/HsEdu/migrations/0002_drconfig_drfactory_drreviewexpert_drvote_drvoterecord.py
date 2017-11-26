# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HsEdu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrConfig',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('startdate', models.CharField(db_column='StartDate', max_length=10)),
                ('stopdate', models.CharField(db_column='StopDate', max_length=10)),
                ('enable', models.IntegerField(blank=True, db_column='Enable', null=True)),
                ('title', models.CharField(db_column='Title', max_length=36)),
                ('introduce', models.CharField(db_column='Introduce', max_length=2000)),
                ('logoimage', models.CharField(db_column='LogoImage', max_length=32)),
                ('zhubanorg', models.CharField(db_column='ZhuBanOrg', max_length=32)),
                ('xiebanorg', models.CharField(db_column='XieBanOrg', max_length=32)),
                ('zhichiorg', models.CharField(db_column='ZhiChiOrg', max_length=32)),
                ('xiezhuorg', models.CharField(db_column='XieZhuOrg', max_length=32)),
                ('xiezhupp', models.CharField(db_column='XieZhuPP', max_length=32)),
                ('erweima', models.CharField(db_column='ErWeiMa', max_length=32)),
            ],
            options={
                'db_table': 'dr_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrFactory',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(db_column='Code', max_length=32)),
                ('name', models.CharField(db_column='Name', max_length=36)),
                ('logoname', models.CharField(db_column='LogoName', max_length=32)),
                ('externinfo1', models.CharField(db_column='ExternInfo1', max_length=128)),
                ('externinfo2', models.CharField(db_column='ExternInfo2', max_length=128)),
                ('externinfo3', models.CharField(db_column='ExternInfo3', max_length=128)),
            ],
            options={
                'db_table': 'dr_factory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrReviewExpert',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(db_column='Code', max_length=32)),
                ('faceimage', models.CharField(db_column='FaceImage', max_length=32)),
                ('info', models.CharField(db_column='Info', max_length=200)),
                ('name', models.CharField(db_column='Name', max_length=36)),
            ],
            options={
                'db_table': 'dr_review_expert',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrVote',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('fcode', models.CharField(blank=True, db_column='FCode', max_length=32, null=True)),
                ('votecount', models.IntegerField(blank=True, db_column='VoteCount', null=True)),
            ],
            options={
                'db_table': 'dr_vote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrVoteRecord',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('ucode', models.CharField(db_column='UCode', max_length=32)),
                ('votedate', models.CharField(db_column='VoteDate', max_length=10)),
                ('voteip', models.CharField(db_column='VoteIp', max_length=15)),
            ],
            options={
                'db_table': 'dr_vote_record',
                'managed': False,
            },
        ),
    ]