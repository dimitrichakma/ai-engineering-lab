# Cost safety

A forgotten cloud resource once cost $290. These rules make sure that never happens again.

## The rules
1. **Local first.** Everything runs on your laptop with Ollama unless a task says otherwise.
2. **No card, or a hard limit.** Use platforms that need no credit card, or that simply stop when
   free credit ends. If a platform needs a card, set a HARD spending limit first. A budget alert
   (like AWS Budgets) only sends an email; it does NOT stop charges.
3. **Idle still bills.** A notebook domain, a GPU, a database, a load balancer: if it exists, it can
   cost money even when you're not using it. Delete, don't just "stop using".
4. **Teardown every time.** Before creating anything online, add it to a `TEARDOWN.md` table
   (see `track3_backend/d1_cloud_deploy/TEARDOWN.md`). When you're done, delete it and tick it.
5. **Check billing the next day.** Set a calendar reminder when you create something. Open the
   billing page of every platform you used. It should say $0.
6. **Separate keys for learning.** Make an API key only for this lab, with a spend limit if the
   provider has one. Delete it when you're done. For Gemini, use a Google account with NO billing
   account attached, so the free tier can't turn into charges.
7. **Secrets stay out.** Keys live in `.env` (git ignored) or the platform's secret settings. Never
   in code, the Docker image, or a commit. If one leaks, delete the key first, then clean up.
8. **CI never calls a paid model.** CI runs with `LLM_PROVIDER=fake`.
9. **App level caps.** Keep the C3 gateway daily limit on for anything public.

## Platforms used in this lab (checked September 2026, check again before you use them)
| Platform | Used in | Card needed? | Notes |
| --- | --- | --- | --- |
| Ollama (local) | everywhere | No | $0 |
| Render free web service | D1 | No | sleeps after 15 min idle |
| Streamlit Community Cloud | D1 | No | public GitHub repo |
| Gemini API free tier | D1 | No | no billing account attached |
| Kaggle Notebooks (GPU) | M3 | No | phone verification, weekly GPU quota |
| Google Colab free | M3 backup | No | sessions end on their own |

Not used on purpose: AWS SageMaker and other paid GPU services, and Hugging Face Docker Spaces
(needs PRO since July 2026).

## If you get a surprise bill
Delete the resource first, then screenshot the bill, then contact the provider's support and ask
for a one time courtesy refund. Many providers grant one for a first mistake by a learner.
