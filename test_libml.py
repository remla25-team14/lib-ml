#!/usr/bin/env python3
"""Test script for lib-ml package"""

import libml

def test_version():
    """Test that version is accessible"""
    version = libml.__version__
    print(f"✅ Version: {version}")
    assert version != "unknown", "Version should not be 'unknown'"
    return True

def test_preprocessing():
    """Test the preprocessing function"""
    test_data = {
        'Review': [
            'This is a GREAT restaurant!',
            'The food was not good.',
            'Amazing service and delicious food!'
        ]
    }
    
    result = libml.preprocess_reviews(test_data)
    print(f"✅ Preprocessing result: {result}")
    
    # Check that we got the expected number of results
    assert len(result) == 3, f"Expected 3 results, got {len(result)}"
    
    # Check that text was processed (lowercase, no punctuation, stemmed)
    assert 'great restaur' in result[0], "First review should contain 'great restaur'"
    assert 'not good' in result[1], "Second review should contain 'not good'"
    
    return True

def test_import():
    """Test that all expected functions are available"""
    assert hasattr(libml, 'preprocess_reviews'), "preprocess_reviews function should be available"
    assert hasattr(libml, '__version__'), "__version__ should be available"
    print("✅ All expected functions are available")
    return True

def test_detailed_preprocessing():
    """Test preprocessing with more detailed checks"""
    test_data = {
        'Review': [
            'The food was NOT good at all!!!',
            'AMAZING restaurant with great service.',
            'Bad experience, would not recommend.'
        ]
    }
    
    result = libml.preprocess_reviews(test_data)
    print(f"✅ Detailed preprocessing result: {result}")
    
    # Check specific preprocessing behaviors
    # 'not' should be preserved (not in stopwords)
    assert 'not' in result[0], "The word 'not' should be preserved"
    
    # Punctuation should be removed
    for processed_review in result:
        assert '!' not in processed_review, "Punctuation should be removed"
        assert ',' not in processed_review, "Punctuation should be removed"
    
    # Text should be lowercase
    for processed_review in result:
        assert processed_review == processed_review.lower(), "Text should be lowercase"
    
    return True

if __name__ == "__main__":
    print("🧪 Testing lib-ml package...")
    print("=" * 50)
    
    try:
        test_import()
        test_version()
        test_preprocessing()
        test_detailed_preprocessing()
        print("\n" + "=" * 50)
        print("🎉 All tests passed! lib-ml is working correctly.")
        print("✅ Version access: Working")
        print("✅ Text preprocessing: Working")
        print("✅ Package structure: Working")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("\n💡 Troubleshooting tips:")
        print("1. Make sure you installed the package: pip install -e .")
        print("2. Check that you're in the lib-ml directory")
        print("3. Ensure Python 3.8+ is installed")
        exit(1) 