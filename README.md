# Restful-Booker API Tests

![API Tests](https://github.com/BrosseauBennet/restful-booker-api-tests/actions/workflows/tests.yml/badge.svg)

API test automation for the [Restful-Booker](https://restful-booker.herokuapp.com) practice API, built with Postman and Python (pytest + requests).

Restful-Booker is a public API that simulates a hotel booking service. It's built for practicing API testing, so no account or API key is needed.

## What's tested

| Area | What it checks |
|---|---|
| Availability | The `/ping` health check responds with 201 |
| Response structure | `/booking` returns a non-empty list of booking IDs; `/booking/{id}` includes the expected fields |
| Performance | Responses come back in under 2 seconds |
| Error handling | Nonexistent booking IDs (0, -1, 999999999) return 404 |

## Project structure

```
api-tests/
├── postman/            # Postman collection (exported JSON)
├── test_bookings.py    # pytest suite: structure, performance, and negative tests
└── test_smoke.py       # quick smoke test that the API is reachable
requirements.txt        # Python dependencies
```

## Setup

Requires Python 3.11 or newer.

```bash
git clone https://github.com/BrosseauBennet/restful-booker-api-tests.git
cd restful-booker-api-tests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the tests

```bash
pytest -v
```

Expected result: all tests pass.

## Postman collection

1. Open Postman and click **Import**.
2. Select the JSON file in `api-tests/postman/`.
3. Run the collection with the Collection Runner. Requests run in order: Ping, Get Booking IDs, Get Booking by ID.

Each request has assertions on status code and response contents, and Ping also checks response time.

## Pytest features used

- **Fixtures:** `booking_id` fetches a real booking ID once so tests don't hard-code one.
- **Parametrization:** one negative test runs against several invalid IDs.

## Known limitations

- Restful-Booker is a shared public service, so an occasionally slow response can make the timing test flaky.
- Coverage is currently limited to read (GET) endpoints.

## Planned next steps

- Authentication and create/update/delete (POST, PUT, DELETE) tests
