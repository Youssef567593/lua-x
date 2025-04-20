from setuptools import setup

setup(
    name='luaX',
    version='1.0',
    description='A package to install Lua and easily write and save Lua scripts.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['luaX'],
    install_requires=[
        # هنا يمكن إضافة أي مكتبات بايثون إذا كان المشروع يعتمد عليها
    ],
    entry_points={
        'console_scripts': [
            'luaX = luaX.main:run',
        ],
    },
)
