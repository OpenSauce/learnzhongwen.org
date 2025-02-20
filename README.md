# LearnZhongwen.org

LearnZhongwen.org is a personal project for learning Django and Chinese. The website features a blog and a flashcard system with spaced repetition (in progress) to help with Chinese vocabulary acquisition.

## Features
- **Blog**: A place to publish progress, insights, and resources related to learning Chinese.
- **Flashcard System (In Progress)**: Implements a spaced repetition algorithm (FSRS) to help reinforce vocabulary retention.

## Tech Stack
- **Backend**: Django
- **Task Queue**: Celery
- **Database**: PostgreSQL
- **Spaced Repetition**: [FSRS](https://github.com/yuin/fsrs) for efficient flashcard scheduling
- **Project**: Based on [nickjj/docker-django-example](https://github.com/nickjj/docker-django-example)
- **HSK Vocabulary**: Uses data from [complete-hsk-vocabulary](https://github.com/drkameleon/complete-hsk-vocabulary)

## Installation & Setup
To set up the project locally:

### Prerequisites
- Docker & Docker Compose

### Running with Docker
```bash
docker-compose up --build
```

## Contribution
This is a personal project, but feel free to open issues or suggest improvements.

## License
This project is under the MIT License.
