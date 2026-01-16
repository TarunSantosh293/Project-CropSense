import requests

def test_root():
    try:
        response = requests.get("http://localhost:8000/")
        print(f"GET /: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"GET / failed: {e}")

def test_analyze():
    try:
        # Create a dummy file
        files = {'file': ('healthy_corn.jpg', b'fake image data', 'image/jpeg')}
        response = requests.post("http://localhost:8000/analyze", files=files)
        print(f"POST /analyze (Healthy): {response.status_code}")
        print(response.json())

        files = {'file': ('blight_potato.jpg', b'fake image data', 'image/jpeg')}
        response = requests.post("http://localhost:8000/analyze", files=files)
        print(f"POST /analyze (Diseased): {response.status_code}")
        print(response.json())
        
    except Exception as e:
        print(f"POST /analyze failed: {e}")

if __name__ == "__main__":
    test_root()
    test_analyze()
