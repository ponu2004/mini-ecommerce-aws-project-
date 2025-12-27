from http.server import BaseHTTPRequestHandler, HTTPServer
import boto3

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Backend is running")

        elif self.path == "/placeOrder":
            sns = boto3.client("sns", region_name="ap-south-1")
            sns.publish(
                TopicArn="REAL_SNS_TOPIC_ARN",
                Message="New Order Placed"
            )
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Order placed successfully!")

server = HTTPServer(("0.0.0.0", 80), Handler)
print("Server started on port 80")
server.serve_forever()
