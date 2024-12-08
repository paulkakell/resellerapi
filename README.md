
---

# Middleware API for Open Order Aggregation

This project provides a middleware application that aggregates open order data from multiple e-commerce platforms. It exposes a RESTful API with OpenAPI documentation, enabling integration with Homepage (`gethomepage.dev`) using the customAPI widget.

## Features
- **Supported Platforms**: Sellbrite, eBay, Shopify, Mercari, Etsy.
- **Data Aggregation**: Calculates the total number of open orders and their total value for each platform.
- **OpenAPI Integration**: Interactive documentation available via Swagger UI.
- **Dockerized Deployment**: Fully self-contained application deployable with Docker.

## Architecture
The application is built using FastAPI and provides asynchronous API calls for efficient data handling. Each platform has its own client module for fetching and processing order data.

## API Endpoints
- `GET /api/orders`: Fetch total open orders and their values for all platforms.

## Setup Instructions

### Prerequisites
- Docker
- API keys for the supported platforms

### Environment Variables
Create a `.env` file based on `.env.example`:
```plaintext
SELLBRITE_API_KEY=your_sellbrite_api_key
EBAY_API_KEY=your_ebay_api_key
SHOPIFY_API_KEY=your_shopify_api_key
MERCARI_API_KEY=your_mercari_api_key
ETSY_API_KEY=your_etsy_api_key
```

### Build and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/paulkarlarthurkell/resellerapi.git
   cd resellerapi
   ```
2. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```
3. Access the API at `http://localhost:8000`:
   - OpenAPI Documentation: `http://localhost:8000/docs`

## Project Structure
```plaintext
middleware-app/
├── app/
│   ├── main.py                # API routes and main application logic
│   ├── platform_clients/      # API client modules for each platform
│   │   ├── sellbrite.py
│   │   ├── ebay.py
│   │   ├── shopify.py
│   │   ├── mercari.py
│   │   ├── etsy.py
│   └── utils.py               # Utility functions
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose configuration
├── requirements.txt           # Python dependencies
└── .env.example               # Environment variable template
```

## Future Enhancements
- Support for additional e-commerce platforms.
- Caching and rate-limiting for improved API performance.
- Advanced analytics and reporting.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
