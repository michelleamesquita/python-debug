import debugpy


debugpy.listen(("0.0.0.0", 5678))

print("Waiting for client to attach...")
debugpy.wait_for_client()