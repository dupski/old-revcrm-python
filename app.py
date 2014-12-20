#!/usr/bin/env python3

if __name__ == "__main__":
    
    from rev import cli
    from rev.app import RevApp

    import settings
    
    app = RevApp('RevCRM', settings)
    
    cli.execute(app)