# Distributed Video Streaming Application

## Overview
A distributed video streaming application built with Flask, MongoDB, AWS S3, Redis, and FFmpeg. The application allows users to:
1. Upload videos, which are transcoded to multiple resolutions.
2. Store metadata in MongoDB.
3. Stream videos directly from AWS S3.
4. Search for videos by title.

## Features
- **Video Upload**: Supports transcoding to `360p`, `720p`, and `1080p` resolutions using FFmpeg.
- **Video Streaming**: Streams videos from AWS S3 URLs.
- **Search Videos**: Provides a search feature to find videos by title.
- **Health Check**: Includes a `/health` endpoint to check application status.

## Technologies Used
- **Backend**: Flask
- **Database**: MongoDB Atlas
- **Caching**: Redis
- **File Storage**: AWS S3
- **Video Transcoding**: FFmpeg
- **Containerization**: Docker and Docker Compose

## Prerequisites
1. Python 3.9+
2. FFmpeg installed
3. MongoDB Atlas account
4. AWS S3 bucket
5. Redis installed or running via Docker

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd distributed_video_streaming
