# -*- coding: utf-8 -*-
# File: __init__.py

# Copyright 2021 Dr. Janis Meyer. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Contains everything that is related to transformation between datapoints
"""
from typing import Callable

from ..utils.file_utils import transformers_available
from .cats import *
from .cocostruct import *
from .maputils import *
from .match import *
from .misc import *
from .pascalstruct import *
from .prodigystruct import *
from .pubstruct import *
from .tpstruct import *
from .xfundstruct import *
from .d2struct import *


if pytorch_available() and transformers_available():
    from .hfstruct import *
    from .laylmstruct import *


# Mapper
Mapper = Callable[[Image], Optional[Image]]
