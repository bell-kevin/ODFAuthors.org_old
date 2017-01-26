# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from odfauthors.policy.testing import ODFAUTHORS_POLICY_INTEGRATION_TESTING
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that odfauthors.policy is properly installed."""

    layer = ODFAUTHORS_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tdf.exttempsitepolicy is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'odfauthors.policy'))

    def test_browserlayer(self):
        """Test that ITdfExttempsitepolicyLayer is registered."""
        from odfauthors.policy.interfaces import (
            IOdfAuthorspolicyLayer)
        from plone.browserlayer import utils
        self.assertIn(IOdfAuthorspolicyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ODFAUTHORS_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['odfauthors.policy'])

    def test_product_uninstalled(self):
        """Test if tdf.exttempsitepolicy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'odfauthors.policy'))

    def test_browserlayer_removed(self):
        """Test that ITdfExttempsitepolicyLayer is removed."""
        from odfauthors.policy.interfaces import IOdfAuthorspolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(IOdfAuthorspolicyLayer, utils.registered_layers())
