"""
TestCases that each integration should inherit.
"""

class PatchTestCase(object):
    """
    TestCase for testing the patch logic of an integration.
    """
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        """
        If tests being done require the module to be deleted/unimported a
        helper is provided in tests.utils.delete_module.
        """
        pass

    def test_patch(self):
        """
        The integration should test that each class, method or function that
        is to be patched is in fact done so.

        For example:

        The redis integration patches the following methods:
        - redis.StrictRedis.execute_command
        - redis.StrictRedis.pipeline
        - redis.Redis.pipeline
        - redis.client.BasePipeline.execute
        - redis.client.BasePipeline.immediate_execute_command

        an appropriate ``test_patch`` would be::

            ddtrace.contrib.redis.patch()
            assert isinstance(redis.StrictRedis.execute_command, wrapt.ObjectProxy)
            assert isinstance(redis.StrictRedis.pipeline, wrapt.ObjectProxy)
            assert isinstance(redis.Redis.pipeline, wrapt.ObjectProxy)
            assert isinstance(redis.client.BasePipeline.execute, wrapt.ObjectProxy)
            assert isinstance(redis.client.BasePipeline.immediate_execute_command, wrapt.ObjectProxy)
        """
        raise NotImplementedError()

    def test_patch_idempotent(self):
        """
        Proper testing should be done to ensure that multiple calls to the
        integration.patch() method are idempotent. That is, that the
        integration does not patch its library more than once.

        An example for what this might look like is again for the redis
        integration::
            ddtrace.contrib.redis.patch()
            ddtrace.contrib.redis.patch()
            assert not isinstance(redis.StrictRedis.execute_command.__wrapped__, wrapt.ObjectProxy)
        """
        raise NotImplementedError()
