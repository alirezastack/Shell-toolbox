try:
            with rabbitpy.Connection('amqp://guest:guest@localhost:5672') as conn:
                with conn.channel() as ch:

                    # Declare an exchange
                    print("declaring an exchange...")
                    xmsg = rabbitpy.Exchange(ch, 'xmsg_topic', 'topic')
                    xmsg.declare()

                    # Publish a message
                    # message = rabbitpy.Message(ch, 'salam')
                    # message.publish('xmsg_topic', 'feedback_message')

                    # Declare a queue and bind it to a topic exchange
                    print("declaring a queue....")
                    queue = rabbitpy.Queue(ch, 'qmsg', False)
                    queue.declare()
                    queue.bind('xmsg_topic', 'feedback_message')

                    # consume message from a queue
                    # for message in rabbitpy.Queue(ch, 'qmsg'):
                    #     print "Message in queue: %s" % message

                    # Consume messages from a queue
                    queue = rabbitpy.Queue(ch, 'qmsg')
                    for message in queue:
                        # message.pprint(True)
                        print(message.json())
                        message.ack()

        except ValueError as ve:
            print("Value error: ", repr(ve))
        except RemoteClosedException as rce:
            print("Remote closed error: ", repr(rce))
        except AMQPAccessRefused as aar:
            print("Authentication failed: ", repr(aar))
        except KeyboardInterrupt:
                    print 'Exited consumer...'
        except Exception as e:
            print("Unknown exception is happened!", repr(e))
