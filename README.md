# Bestattungshaus Riedel 🕊️

A modern, professional, and empathetic website for a funeral services business. Built with **Django**, this site is designed to provide information about funeral services, ceremonies, and precautions in a respectful and accessible manner.

## ✨ Features

- **Multilingual Support**: Fully translated into German, English, and Ukrainian using Django's `i18n` and `modeltranslation`.
- **Responsive Design**: Optimized for all devices—from desktop monitors to mobile phones.
- **Service Management**: Detailed sections for different funeral types:
  - Traditional Burials
  - Forest and Sea Burials
  - Funeral Speeches & Individual Farewells
- **Empathy-First UI**: Soft color palettes, elegant typography (Playfair Display & Open Sans), and smooth animations.
- **Deployment Ready**: Fully containerized with Docker and Nginx.

## 🛠️ Tech Stack

- **Backend**: Python 3.11, Django 5.x
- **Frontend**: Vanilla CSS (Mobile-first), HTML5, FontAwesome
- **Serving**: Gunicorn, WhiteNoise (static file compression)
- **Deployment**: Docker, Docker Compose, Nginx

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- [Optional] Docker & Docker Compose

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/funeral-services-site.git
   cd funeral-services-site
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Copy `.env.example` to `.env` and configure accordingly:
   ```bash
   cp .env.example .env
   ```

5. **Run migrations and start server**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### 🐳 Running with Docker

To simulate the production environment or for easy setup:

```bash
docker-compose up --build
```
Access the site at `http://localhost`.

## 📦 Project Structure

- `core/`: Main app handling static pages and general logic.
- `services/`: App managing service listings and details.
- `static/`: Global CSS, images, and Javascript.
- `templates/`: HTML components and page layouts.
- `config/`: Django project configuration (settings, URLs).

## 📄 Deployment

The project is pre-configured for production deployment via Nginx and Gunicorn. Detailed deployment steps can be found in the [walkthrough.md](./walkthrough.md) (internal documentation) or by following standard Docker deployment practices.

---

*Bestattungshaus Riedel — At your side in difficult times.*
