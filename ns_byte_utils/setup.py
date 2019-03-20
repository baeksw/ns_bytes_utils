try:
    from setuptools import setup
except:
    from distutils.core import setup
#esudp.udp_server.start_server

dependencies = ['docopt']

setup(
    name='ns_byte_utils',
    version='0.0.1',
    description='bytes & binary utils',
    author='seungwoo.BAEK',
    author_email='dohaskell7@gmail.com',
    install_requires=dependencies,
    packages=[
        'ns',
        'ns.bytes',
    ],
)
 
