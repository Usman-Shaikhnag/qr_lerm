# This file is part of lims_email module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

try:
    from trytond.modules.lims_email.tests.test_lims_email import suite
except ImportError:
    from .test_lims_email import suite

__all__ = ['suite']
