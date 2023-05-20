#!/usr/bin/python3
"""
Test for storage
"""

class Test_fileStorage(unittest.Testcase):
    """Test FileStorage Class"""
    def test_instances(self):
        """chequeamos instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)
    
    def test_doc(self):
        """Teest Docstrings"""
        self.assertIsNotNone(FileStore.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()

