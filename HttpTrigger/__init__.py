import os
import sys
import logging
import json
import azure.functions as func

from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage, TextBase64EncodePolicy, BinaryBase64DecodePolicy
from azure.core.exceptions import ResourceExistsError

message_body = {
    'message': 'Here is some text'
}

queue_name = 'processing'


def create_queue_service():
    conn_str = os.environ['AzureWebJobsStorage']
    queue_service = QueueClient.from_connection_string(
        conn_str=conn_str,
        queue_name=queue_name,
        message_encode_policy=TextBase64EncodePolicy(),
        message_decode_policy=BinaryBase64DecodePolicy())
    try:
        queue_service.create_queue()
        logging.info(f'Created queue {queue_name}')
        return queue_service
    except ResourceExistsError:
        logging.info(f'Queue {queue_name} already exists')
        return queue_service


def add_message_to_queue(queue_service):
    logging.info("Add message to queue")
    queue_service.send_message(json.dumps(message_body))


def peek_at_messages(queue_service):
    logging.info("\nPeek at the messages in the queue...")

    # Peek at messages in the queue
    peeked_messages = queue_service.peek_messages(10)

    for peeked_message in peeked_messages:
        # Display the message
        logging.info(f'Message: {peeked_message.content}')


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        logging.info("Azure Queue storage - Python quickstart sample")
        # queue_service = create_queue_service()

        # add_message_to_queue(queue_service)
        # peek_at_messages(queue_service)

        return func.HttpResponse('Passed', status_code=200)
    except Exception as e:
        logging.error(f'Exception: {e}')
        return func.HttpResponse('failed', status_code=200)
