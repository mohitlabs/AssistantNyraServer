# MIT License

# Copyright (c) 2023 MohitLabs

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from fastapi import FastAPI

app = FastAPI()

username = "Mohit"

request_and_response = {
    "play some music": f"OK {username}. Playing some random music from your favourite library.",
    "wikipedia": "Searching wikipedia",
    "open google": "Opening Google for you. Just wait.",
    "open gmail": "Opening your Gmail. Just wait.",
    "open youtube": "Opening Youtube for you. Just wait.",
    "open github": "Opening your Github. Just wait.",
    "open stackoverflow": "Opening Stack Overflow for you. Just wait."
}

@app.get("/{query}")
async def respond(query):
    for request, response in request_and_response.items():
        if request in query:
            return response
    return f"{username}, your query didn't match with my database. Try something else."
