{
    "builds": [{
        "src": "HQ/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
    }],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "HQ/wsgi.py"
        }
    ]
}
