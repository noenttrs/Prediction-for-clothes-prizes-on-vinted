from sklearn2onnx import convert
from skl2onnx.common.data_types import FloatTensorType

initial_type = [('float_input', FloatTensorType([None, num_features]))]
onnx_model = convert(model, initial_types=initial_type)
