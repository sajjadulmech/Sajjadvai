#!/usr/bin/env python3
"""
ClearTapLab Automated 4-Tier E2E Test Suite Runner
CLI entry point for executing all test tiers with summary reporting,
granular filtering, JSON output, and strict pass/fail exit codes.

Usage:
  python tests/run_e2e_tests.py
  python tests/run_e2e_tests.py --tier 1,2
  python tests/run_e2e_tests.py --tier 3 --verbose
  python tests/run_e2e_tests.py --json
  python tests/run_e2e_tests.py --failfast
  python tests/run_e2e_tests.py --list
"""

import sys
import os
import time
import json
import argparse
import unittest

# Ensure UTF-8 output encoding on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Ensure tests module is importable
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from tests.test_tier1_features import TestTier1FeatureCoverage
from tests.test_tier2_boundaries import TestTier2BoundaryAndEdgeCases
from tests.test_tier3_cross_feature import TestTier3CrossFeatureCombinations
from tests.test_tier4_user_scenarios import TestTier4RealWorldScenarios


TIER_MAPPING = {
    1: {
        "name": "Tier 1: Feature & Content Coverage",
        "description": "Validates 20 guides for metadata, H1, badge, spec-box, table, FAQs, and science",
        "suite_class": TestTier1FeatureCoverage
    },
    2: {
        "name": "Tier 2: Boundary & Corner Cases",
        "description": "Tests live search injection, category boundaries, modal lifecycle, and calculator inputs",
        "suite_class": TestTier2BoundaryAndEdgeCases
    },
    3: {
        "name": "Tier 3: Cross-Feature Combinations",
        "description": "Tests search + filter combos, modal cross-links, triage links, and hub navigation",
        "suite_class": TestTier3CrossFeatureCombinations
    },
    4: {
        "name": "Tier 4: Real-World User Scenarios",
        "description": "Tests full end-to-end user journeys (RO, Well Water, Hardness Softener, CCR Report)",
        "suite_class": TestTier4RealWorldScenarios
    }
}


class CustomTestResult(unittest.TestResult):
    """Captures detailed execution metrics for reporting."""

    def __init__(self, verbose=False):
        super().__init__()
        self.verbose = verbose
        self.successes = []
        self.test_timings = {}
        self._current_test_start = None

    def startTest(self, test):
        super().startTest(test)
        self._current_test_start = time.perf_counter()

    def addSuccess(self, test):
        super().addSuccess(test)
        elapsed = time.perf_counter() - self._current_test_start
        self.successes.append((test, elapsed))
        if self.verbose:
            doc = (test.shortDescription() or test._testMethodName).strip()
            print(f"  [PASS] {test._testMethodName} ({elapsed:.3f}s) - {doc}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        elapsed = time.perf_counter() - self._current_test_start
        if self.verbose:
            print(f"  [FAIL] {test._testMethodName} ({elapsed:.3f}s)")

    def addError(self, test, err):
        super().addError(test, err)
        elapsed = time.perf_counter() - self._current_test_start
        if self.verbose:
            print(f"  [ERROR] {test._testMethodName} ({elapsed:.3f}s)")

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        if self.verbose:
            print(f"  [SKIP] {test._testMethodName} - {reason}")


def run_tier(tier_num, verbose=False, failfast=False):
    """Executes a single test tier and returns summary metrics."""
    tier_info = TIER_MAPPING.get(tier_num)
    if not tier_info:
        raise ValueError(f"Unknown tier: {tier_num}")

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(tier_info["suite_class"])
    
    result = CustomTestResult(verbose=verbose)
    if failfast:
        result.failfast = True

    start_time = time.perf_counter()
    suite.run(result)
    total_time = time.perf_counter() - start_time

    total_run = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(result.skipped)
    passed = len(result.successes)

    return {
        "tier": tier_num,
        "name": tier_info["name"],
        "description": tier_info["description"],
        "total": total_run,
        "passed": passed,
        "failed": failures,
        "errors": errors,
        "skipped": skipped,
        "duration_seconds": total_time,
        "pass_rate": (passed / total_run * 100.0) if total_run > 0 else 0.0,
        "failure_details": [
            {
                "test": test._testMethodName,
                "description": test.shortDescription() or "",
                "traceback": err
            }
            for test, err in result.failures
        ],
        "error_details": [
            {
                "test": test._testMethodName,
                "description": test.shortDescription() or "",
                "traceback": err
            }
            for test, err in result.errors
        ]
    }


def list_tests():
    """Lists all tests available in each tier without executing."""
    print("=" * 80)
    print("ClearTapLab E2E Test Suite - Available Test Inventory")
    print("=" * 80)
    total_count = 0
    for tier_num, info in sorted(TIER_MAPPING.items()):
        print(f"\n[{info['name']}]")
        print(f"  Description: {info['description']}")
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(info["suite_class"])
        for test in suite:
            total_count += 1
            doc = (test.shortDescription() or "").strip()
            print(f"    - {test._testMethodName}: {doc}")
    print("\n" + "=" * 80)
    print(f"Total Available Test Methods: {total_count}")
    print("=" * 80)


def print_ascii_summary(results, total_duration):
    """Renders a structured ASCII table of test results."""
    print("\n" + "=" * 88)
    print("                         CLEARTAPLAB E2E TEST EXECUTION SUMMARY                         ")
    print("=" * 88)
    print(f"{'Tier':<35} | {'Total':<6} | {'Passed':<7} | {'Failed':<7} | {'Errors':<7} | {'Pass %':<7} | {'Time'}")
    print("-" * 88)
    
    total_tests = 0
    total_passed = 0
    total_failed = 0
    total_errors = 0
    total_skipped = 0

    for r in results:
        total_tests += r["total"]
        total_passed += r["passed"]
        total_failed += r["failed"]
        total_errors += r["errors"]
        total_skipped += r["skipped"]
        
        status_color = "PASS" if (r["failed"] == 0 and r["errors"] == 0) else "FAIL"
        print(
            f"{r['name']:<35} | "
            f"{r['total']:<6} | "
            f"{r['passed']:<7} | "
            f"{r['failed']:<7} | "
            f"{r['errors']:<7} | "
            f"{r['pass_rate']:>6.1f}% | "
            f"{r['duration_seconds']:.3f}s"
        )

    print("-" * 88)
    overall_pass_rate = (total_passed / total_tests * 100.0) if total_tests > 0 else 0.0
    print(
        f"{'OVERALL TOTALS':<35} | "
        f"{total_tests:<6} | "
        f"{total_passed:<7} | "
        f"{total_failed:<7} | "
        f"{total_errors:<7} | "
        f"{overall_pass_rate:>6.1f}% | "
        f"{total_duration:.3f}s"
    )
    print("=" * 88)

    # Print failure details if any exist
    any_failures = any(r["failed"] > 0 or r["errors"] > 0 for r in results)
    if any_failures:
        print("\n" + "!" * 88)
        print("                                  FAILURE DETAILS                                       ")
        print("!" * 88)
        for r in results:
            if r["failed"] > 0 or r["errors"] > 0:
                print(f"\n>>> {r['name']} Failures:")
                for f in r["failure_details"]:
                    print(f"\n  [FAILED] {f['test']} - {f['description']}")
                    # Print first 4 lines of traceback or assertion message
                    lines = [l for l in f["traceback"].strip().split("\n") if l.strip()]
                    last_lines = lines[-4:] if len(lines) >= 4 else lines
                    for line in last_lines:
                        print(f"    {line}")
                for e in r["error_details"]:
                    print(f"\n  [ERROR] {e['test']} - {e['description']}")
                    lines = [l for l in e["traceback"].strip().split("\n") if l.strip()]
                    last_lines = lines[-4:] if len(lines) >= 4 else lines
                    for line in last_lines:
                        print(f"    {line}")
        print("\n" + "!" * 88)

    if overall_pass_rate == 100.0 and total_tests > 0:
        print("\n>>> ALL TESTS PASSED SUCCESSFULLY! (Exit Code 0)\n")
    else:
        print(f"\n>>> TEST SUITE COMPLETED WITH FAILURES: {total_failed + total_errors} issue(s) detected. (Exit Code 1)\n")


def main():
    parser = argparse.ArgumentParser(
        description="ClearTapLab 4-Tier Automated E2E Test Suite Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--tier", "-t",
        default="all",
        help="Specify tiers to run (e.g. '1', '1,2', '3,4', or 'all'). Default: 'all'"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Display detailed progress and method names during test execution"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results strictly in JSON format"
    )
    parser.add_argument(
        "--failfast", "-f",
        action="store_true",
        help="Stop suite execution on the first failure or error"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all available tests by tier and exit"
    )

    args = parser.parse_args()

    if args.list:
        list_tests()
        sys.exit(0)

    # Determine tiers to execute
    if args.tier.lower() == "all":
        tiers_to_run = [1, 2, 3, 4]
    else:
        try:
            tiers_to_run = [int(t.strip()) for t in args.tier.split(",") if t.strip()]
            for t in tiers_to_run:
                if t not in TIER_MAPPING:
                    print(f"Error: Invalid tier number '{t}'. Must be one of 1, 2, 3, 4.", file=sys.stderr)
                    sys.exit(2)
        except ValueError:
            print(f"Error: Could not parse tier argument '{args.tier}'.", file=sys.stderr)
            sys.exit(2)

    suite_start = time.perf_counter()
    results = []

    if not args.json:
        print("=" * 88)
        print("                   STARTING CLEARTAPLAB AUTOMATED E2E TEST SUITE                 ")
        print(f"  Target Tiers: {tiers_to_run} | Verbose: {args.verbose} | FailFast: {args.failfast}")
        print("=" * 88)

    for tier_num in tiers_to_run:
        if args.verbose and not args.json:
            print(f"\n>>> Running {TIER_MAPPING[tier_num]['name']}...")
        tier_res = run_tier(tier_num, verbose=args.verbose, failfast=args.failfast)
        results.append(tier_res)
        if args.failfast and (tier_res["failed"] > 0 or tier_res["errors"] > 0):
            break

    total_duration = time.perf_counter() - suite_start

    if args.json:
        output_payload = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_duration_seconds": total_duration,
            "tiers": results,
            "overall_passed": all(r["failed"] == 0 and r["errors"] == 0 for r in results),
            "total_tests": sum(r["total"] for r in results),
            "total_passed": sum(r["passed"] for r in results),
            "total_failed": sum(r["failed"] for r in results),
            "total_errors": sum(r["errors"] for r in results)
        }
        print(json.dumps(output_payload, indent=2))
    else:
        print_ascii_summary(results, total_duration)

    all_passed = all(r["failed"] == 0 and r["errors"] == 0 for r in results)
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
