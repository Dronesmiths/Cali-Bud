# Cali-Bud Delivery: Content & Newsletter Queue

Use this checklist to track the rollout of the 50 high-authority content pieces. Mark as `[x]` only after the page is live and CloudFront cache is invalidated.

## Phase 1: The Authority Foundation (1-10)
- [x] **01: Cornerstone Guide** - The Ultimate Guide to Cannabis Delivery in Antelope Valley
- [x] **02: Locality Anchor** - Why Cali-Bud is Palmdale's Fastest Delivery Service
- [/] **03: Product Deep Dive** - Top 5 Sleep-Aid Edibles Available in Lancaster (Title: Top 5 Strains for Sleep)
- [x] **04: PAA Capture** - Is Weed Delivery Legal in Palmdale? (Compliance Guide)
- [ ] **05: Strain Spotlight** - Blue Dream: Why It's the AV's Favorite Hybrid
- [ ] **06: Product Deep Dive** - Vape Cartridges: Live Resin vs Distillate Explained
- [ ] **07: Pro Tip** - How to Keep Your Stash Fresh in the High Desert Heat
- [ ] **08: Neighborhood Spotlight** - Delivery Times for Quartz Hill & West Lancaster
- [ ] **09: PAA Capture** - Can I order weed to a hotel in Palmdale?
- [ ] **10: Locality Anchor** - Rosamond Cannabis Delivery: Rules & ETA
- [x] **Launch Update** - Cali-Bud is Live on calibud.club!

## Phase 2: Strategic Expansion (11-30)
- [ ] **11: Locality Anchor** - Lake Los Angeles Delivery Guide
- [ ] **12: PAA Capture** - What is the tax on marijuana in California 2026?
- [ ] **13: Product Deep Dive** - CBD for Pet Anxiety: What You Need to Know
- [ ] **14: Strain Spotlight** - OG Kush: The Classic That Never Fades
- [ ] **15: Cornerstone Pillar** - A Beginner's Guide to Dosing Edibles Safely
- [ ] **16-30:** ...

## Phase 3: Domain Dominance (31-50)
- [ ] **31:** ...
- [ ] **50:** ...

> [!IMPORTANT]
> **Deployment Rule**: Every time a checkbox is marked `[x]`, you must:
> 1. Sync the repo: `git add . && git commit -m "feat: deploy content piece #[XX]" && git push`
> 2. Sync S3: `aws s3 sync . s3://cali-bud-deliveries --delete --exclude ".git/*" --exclude ".github/*" --exclude "factory/*" --profile mediusa`
> 3. Invalidate: `aws cloudfront create-invalidation --distribution-id E48DSMEP69HP2 --paths "/news/*" "/blog/*" --profile mediusa`
