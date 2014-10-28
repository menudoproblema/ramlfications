#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Spotify AB
from __future__ import absolute_import, division, print_function

import os

from ramlfications.validate import RAMLValidationError, validate

from .base import BaseTestCase


class TestValidateRAML(BaseTestCase):
    def setUp(self):
        self.here = os.path.abspath(os.path.dirname(__file__))

    def test_validate_raml_header(self):
        invalid_header = "examples/incorrect-raml-header.raml"
        raml_file = os.path.join(self.here, invalid_header)
        expected_msg = 'Not a valid RAML header: #%FOO.'

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_raml_version(self):
        invalid_header = "examples/invalid-version-raml-header.raml"
        raml_file = os.path.join(self.here, invalid_header)
        expected_msg = 'Not a valid version of RAML: 0.9.'

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_title(self):
        no_title = "examples/validate/no-title.raml"
        raml_file = os.path.join(self.here, no_title)
        expected_msg = 'RAML File does not define an API title.'

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_version(self):
        no_version = "examples/validate/no-version.raml"
        raml_file = os.path.join(self.here, no_version)
        expected_msg = 'RAML File does not define an API version.'

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_base_uri(self):
        no_base_uri = "examples/validate/no-base-uri.raml"
        raml_file = os.path.join(self.here, no_base_uri)
        expected_msg = 'RAML File does not define the baseUri.'

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_base_params(self):
        no_default_param = "examples/validate/no-default-base-uri-params.raml"
        raml_file = os.path.join(self.here, no_default_param)
        expected_msg = "'domainName' needs a default parameter."

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_resource_responses(self):
        invalid_responses = "examples/validate/responses.raml"
        raml_file = os.path.join(self.here, invalid_responses)

        expected_msg = "'anInvalidKey' not a valid Response parameter."

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_docs_title(self):
        docs_no_title = "examples/validate/docs-no-title.raml"
        raml_file = os.path.join(self.here, docs_no_title)

        expected_msg = "API Documentation requires a title."

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_docs_content(self):
        no_content = "examples/validate/docs-no-content.raml"
        raml_file = os.path.join(self.here, no_content)
        expected_msg = "API Documentation requires content defined."

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)

    def test_validate_security_scheme(self):
        invalid_sec_scheme = "examples/validate/invalid-security-scheme.raml"
        raml_file = os.path.join(self.here, invalid_sec_scheme)
        expected_msg = "'Invalid Scheme' is not a valid Security Scheme."

        try:
            validate(raml_file)
            self.assertFail()
        except RAMLValidationError as e:
            self.assertEqual(e.message, expected_msg)
