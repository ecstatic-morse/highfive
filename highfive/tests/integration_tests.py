from highfive import newpr, payload
from highfive.tests import base
from nose.plugins.attrib import attr

@attr(type='integration')
class TestIsNewContributor(base.BaseTest):
    def setUp(self):
        super(TestIsNewContributor, self).setUp()

        self.payload = payload.Payload({'repository': {'fork': False}})

    def test_real_contributor_true(self):
        self.assertFalse(
            newpr.is_new_contributor(
                'nrc', 'rust-lang', 'rust', '', self.payload
            )
        )

    def test_real_contributor_false(self):
        self.assertTrue(
            newpr.is_new_contributor(
                'octocat', 'rust-lang', 'rust', '', self.payload
            )
        )

    def test_fake_user(self):
        self.assertTrue(
            newpr.is_new_contributor(
                'fjkesfgojsrgljsdgla', 'rust-lang', 'rust', '', self.payload
            )
        )