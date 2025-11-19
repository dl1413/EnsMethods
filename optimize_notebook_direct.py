#!/usr/bin/env python3
"""
Direct optimization script for the Jupyter notebook
Makes minimal, targeted changes to improve performance
"""

import json
import sys

def optimize_notebook(notebook_path):
    """Load, optimize, and save the notebook"""
    
    print(f"Loading notebook: {notebook_path}")
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    changes = []
    
    # Cell 38 - Random Forest GridSearchCV
    cell_38_code = ''.join(notebook['cells'][38]['source'])
    if 'grid_search = GridSearchCV(rf_classifier, param_grid, cv=5, scoring=\'accuracy\')' in cell_38_code:
        new_code = cell_38_code.replace(
            'grid_search = GridSearchCV(rf_classifier, param_grid, cv=5, scoring=\'accuracy\')',
            'grid_search = GridSearchCV(rf_classifier, param_grid, cv=5, scoring=\'accuracy\', n_jobs=-1)'
        )
        notebook['cells'][38]['source'] = [new_code]
        changes.append("Cell 39 (index 38): Added n_jobs=-1 to GridSearchCV (Random Forest)")
    
    # Cell 42 - Gradient Boosting GridSearchCV
    cell_42_code = ''.join(notebook['cells'][42]['source'])
    if 'grid_search = GridSearchCV(gb_classifier, param_grid, cv=5, scoring=\'accuracy\')' in cell_42_code:
        new_code = cell_42_code.replace(
            'grid_search = GridSearchCV(gb_classifier, param_grid, cv=5, scoring=\'accuracy\')',
            'grid_search = GridSearchCV(gb_classifier, param_grid, cv=5, scoring=\'accuracy\', n_jobs=-1)'
        )
        notebook['cells'][42]['source'] = [new_code]
        changes.append("Cell 43 (index 42): Added n_jobs=-1 to GridSearchCV (Gradient Boosting)")
    
    # Cell 46 - AdaBoost GridSearchCV
    cell_46_code = ''.join(notebook['cells'][46]['source'])
    if 'grid_search = GridSearchCV(adaboost_classifier, param_grid, cv=5, scoring=\'accuracy\')' in cell_46_code:
        new_code = cell_46_code.replace(
            'grid_search = GridSearchCV(adaboost_classifier, param_grid, cv=5, scoring=\'accuracy\')',
            'grid_search = GridSearchCV(adaboost_classifier, param_grid, cv=5, scoring=\'accuracy\', n_jobs=-1)'
        )
        notebook['cells'][46]['source'] = [new_code]
        changes.append("Cell 47 (index 46): Added n_jobs=-1 to GridSearchCV (AdaBoost)")
    
    # Cell 50 - Bagging GridSearchCV
    cell_50_code = ''.join(notebook['cells'][50]['source'])
    if 'grid_search = GridSearchCV(bagging_classifier, param_grid, cv=5, scoring=\'accuracy\')' in cell_50_code:
        new_code = cell_50_code.replace(
            'grid_search = GridSearchCV(bagging_classifier, param_grid, cv=5, scoring=\'accuracy\')',
            'grid_search = GridSearchCV(bagging_classifier, param_grid, cv=5, scoring=\'accuracy\', n_jobs=-1)'
        )
        notebook['cells'][50]['source'] = [new_code]
        changes.append("Cell 51 (index 50): Added n_jobs=-1 to GridSearchCV (Bagging)")
    
    # Cell 85 - Replace iterrows() with itertuples()
    cell_85_code = ''.join(notebook['cells'][85]['source'])
    if 'for idx, row in top_3.iterrows():' in cell_85_code:
        # Replace iterrows with a more efficient pattern
        # Since we're just printing and the dataframe is small (3 rows), 
        # we'll add a comment explaining the issue
        new_code = cell_85_code.replace(
            'for idx, row in top_3.iterrows():',
            'for idx, row in top_3.iterrows():  # Performance note: iterrows is slow; OK for small DataFrames'
        )
        notebook['cells'][85]['source'] = [new_code]
        changes.append("Cell 86 (index 85): Added performance comment about iterrows()")
    
    # Save the optimized notebook
    print(f"\nSaving optimized notebook...")
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    # Print summary
    print("\n" + "=" * 80)
    print("OPTIMIZATION SUMMARY")
    print("=" * 80)
    print(f"Total changes applied: {len(changes)}\n")
    for change in changes:
        print(f"  ✓ {change}")
    
    print("\n" + "=" * 80)
    print("EXPECTED PERFORMANCE IMPROVEMENTS")
    print("=" * 80)
    print("  • GridSearchCV parallelization: 4-8x faster on multi-core systems")
    print("  • Hyperparameter tuning time reduced significantly")
    print("  • Better CPU utilization during model training")
    print("\n✓ Optimization complete!")
    
    return len(changes)

if __name__ == "__main__":
    notebook_file = "STAT 790- CAPSTONE PROJECT (1).ipynb"
    
    try:
        changes_count = optimize_notebook(notebook_file)
        sys.exit(0 if changes_count > 0 else 1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
