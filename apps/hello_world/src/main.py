from logger import Logger

logger = Logger("Hello_World").get_logger()

logger.info("Applicaytion Started ...")

print("Hello K8s! Welcome to the first app running on Kubernetes.")

logger.info("Application Finished!")