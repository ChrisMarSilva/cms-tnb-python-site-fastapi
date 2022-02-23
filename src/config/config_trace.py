from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor


tracer = trace.get_tracer(__name__)
resource = Resource.create({SERVICE_NAME: "TamoNaBolsa"})
provider = TracerProvider(resource=resource)


def config_trace_init():
    trace.set_tracer_provider(tracer_provider=provider)
    jaeger_exporter = JaegerExporter(agent_host_name='localhost', agent_port=6831)
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)