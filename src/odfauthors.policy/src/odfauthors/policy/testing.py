# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import helpers

import odfauthors.policy
import collective.MockMailHost


class OdfauthorspolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=odfauthors.policy)
        self.loadZCML(package=collective.MockMailHost)
        z2.installProduct(app, 'collective.MockMailHost')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'odfauthors.policy:default')
        applyProfile(portal, 'collective.MockMailHost:default')
        helpers.quickInstallProduct(portal, 'collective.MockMailHost')
        setRoles(portal, TEST_USER_ID, ['Manager'])

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'collective.MockMailHost')


ODFAUTHORS_POLICY_FIXTURE = OdfauthorspolicyLayer()

ODFAUTHORS_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ODFAUTHORS_POLICY_FIXTURE,),
    name="OdfauthorspolicyLayer:IntegrationTesting"
)


ODFAUTORS_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ODFAUTHORS_POLICY_FIXTURE,),
    name='OdfauthorspolicyLayer:FunctionalTesting'
)


TDF_EXTTEMPSITEPOLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ODFAUTHORS_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='OdfauthorspolicyLayer:AcceptanceTesting'
)
