#!/usr/bin/env python
from fnest import fnest
import os

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 3933))
	fnest.run(host='0.0.0.0', port=port)
