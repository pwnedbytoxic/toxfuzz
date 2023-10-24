# ToxFuzz - Simple Python API Fuzzer

ToxFuzz is a basic API fuzzer written in Python using standard libraries. It's designed to help you identify potential vulnerabilities in your web APIs by sending various input payloads and observing the behavior of the API in response. This tool is lightweight and easy to use, making it a valuable addition to your security testing toolkit. It may also be used for bug bounty purposes, but I take no responsibility for any unauthorized access the use of this tool may warrant.

## Features

- Send a variety of payloads to your API endpoint.
- Observe the API's response for potential vulnerabilities.
- Built with standard Python libraries for easy setup and usage.

## Getting Started

Follow these simple steps to get ToxFuzz up and running:

### Prerequisites

1. Python 3.x is installed on your system with standard libaries (requests & sys).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/toxfuzz.git
   ```
2. `cd` into the directory:
   ```bash
   cd toxfuzz
   ```
4.   Run the program with the following syntax:
   ```bash
   cat medium.txt | python3 toxfuzz.py
   ```
  - You must change `https://example.com/api/` into your own api
4.  Toxfuzz will start sending the payloads to the specified API endpoint and display the responses.

---

Happy hacking!!!
