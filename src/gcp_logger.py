import logging
from google.cloud.logging.handlers import CloudLoggingHandler
from custom_exceptions import ArgumentCompatibilityException


def make_logger(logger_name: str, cloud: bool=False, project_id: str=None) -> logging.Logger:
    """Utility function to create an instance of logging.Logger that either prints to stdout or gets passed to a CloudLoggingHandler

    Parameters
    ----------
    logger_name : str
        Name of the Logger object
    cloud : bool, optional
        Whether the Logger object should be handled by a GCP CloudLoggingHandler, by default False
    project_id : str, optional
        Project ID for GCP project to which the CloudLoggingHandler will write (required if cloud=True), by default None

    Returns
    -------
    logging.Logger
        Logger object for use within a module or script
    """
    project_id = False if not project_id else project_id
    logger = logging.getLogger(name=logger_name)

    # the custom exception used below functions similarly to the following assert statement:
    # assert not cloud and not project_id, f"Argument mismatch -- cloud={cloud} and project_id={project_id}"
    if cloud and not project_id:
        raise ArgumentCompatibilityException([cloud, project_id])
