#### 4. **الملف `main.py`**
- هذا هو الملف الذي سيتحكم في الوظائف الرئيسية للحزمة، مثل كتابة الأكواد وحفظها.

```python
import os

def run():
    print("Welcome to LuaX - Lua Script Writer")

    while True:
        # الحصول على إدخال من المستخدم
        code = input("Enter Lua code (type 'exit' to quit): ")
        
        if code.lower() == 'exit':
            print("Goodbye!")
            break

        # حفظ الكود في ملف
        with open("script.lua", "w") as file:
            file.write(code)
        
        print("Code saved in script.lua")
        print("Running the Lua script...")

        # تشغيل الكود باستخدام Lua
        os.system("lua script.lua")
