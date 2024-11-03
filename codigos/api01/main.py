import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="CPU Processing API",
    description="API with light and heavy CPU processing endpoints using Fibonacci calculations",
    version="1.0.0",
)


class ProcessingResponse(BaseModel):
    """
    Response model for processing endpoints
    """

    result: int
    processing_time: float
    endpoint: str

    class Config:
        schema_extra = {
            "example": {"result": 6765, "processing_time": 0.0021, "endpoint": "light"}
        }


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@app.post(
    "/light",
    response_model=ProcessingResponse,
    summary="Light CPU Processing",
    description="Performs light CPU processing by calculating fibonacci(20)",
    response_description="Returns the fibonacci result, processing time, and endpoint name",
)
def light_processing():
    """
    Performs light CPU processing:
    - Calculates fibonacci(35)
    - Measures processing time
    - Returns result and metrics

    Returns:
        ProcessingResponse: Object containing result, processing time, and endpoint name
    """
    start_time = time.time()
    result = fibonacci(35)  # Light processing
    end_time = time.time()

    return ProcessingResponse(
        result=result, processing_time=end_time - start_time, endpoint="light"
    )


@app.post(
    "/heavy",
    response_model=ProcessingResponse,
    summary="Heavy CPU Processing",
    description="Performs heavy CPU processing by calculating fibonacci(35)",
    response_description="Returns the fibonacci result, processing time, and endpoint name",
)
def heavy_processing():
    """
    Performs heavy CPU processing:
    - Calculates fibonacci(65)
    - Measures processing time
    - Returns result and metrics

    Returns:
        ProcessingResponse: Object containing result, processing time, and endpoint name
    """
    start_time = time.time()
    result = fibonacci(65)  # Heavy processing
    end_time = time.time()

    return ProcessingResponse(
        result=result, processing_time=end_time - start_time, endpoint="heavy"
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
