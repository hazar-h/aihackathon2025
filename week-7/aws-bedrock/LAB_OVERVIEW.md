# AWS Bedrock Hands-On Demo Lab - Complete Package

## 📋 Package Contents

This comprehensive lab package includes everything you need to master AWS Bedrock:

### 1. Main Lab Guide (`bedrock_lab.md`)
**Complete hands-on lab with 8 modules covering:**
- ✅ Model Selection & Comparison
- ✅ Prompt Management & Engineering
- ✅ Knowledge Bases (RAG Implementation)
- ✅ Guardrails Configuration
- ✅ Model Fine-Tuning
- ✅ Data Automation
- ✅ Model Evaluation
- ✅ End-to-End Application Development

**Duration:** 3-4 hours  
**Difficulty:** Intermediate  
**Estimated Cost:** $10-30 (with proper cleanup)

### 2. Quick Reference Guide (`quick_reference.md`)
**Essential cheat sheet containing:**
- Common API calls with code examples
- Model IDs quick reference
- Pricing information
- Troubleshooting guide
- IAM policy templates
- Best practices checklist

### 3. Automated Setup Script (`setup_lab.sh`)
**One-command environment setup:**
- Creates S3 buckets and folder structure
- Generates sample documents
- Sets up IAM roles and policies
- Installs Python dependencies
- Creates configuration files
- Includes helper utilities

---

## 🚀 Getting Started

### Prerequisites

Before starting the lab, ensure you have:

1. **AWS Account** with appropriate permissions
2. **AWS CLI** installed and configured
3. **Python 3.8+** installed
4. **boto3** library installed
5. **Basic understanding** of AI/ML concepts

### Quick Start (3 Steps)

#### Step 1: Run Setup Script
```bash
chmod +x setup_lab.sh
./setup_lab.sh
```

#### Step 2: Enable Model Access
1. Go to AWS Console → Amazon Bedrock → Model access
2. Click "Manage model access"
3. Enable these models:
   - ✅ Anthropic Claude 3.5 Sonnet
   - ✅ Anthropic Claude 3 Haiku  
   - ✅ Meta Llama 3.2 (11B & 90B)
   - ✅ Amazon Titan Text & Embeddings
   - ✅ AI21 Jurassic-2
4. Wait for approval (usually instant)

#### Step 3: Start the Lab
```bash
# Load configuration
source bedrock_lab_config.env

# Test access
python bedrock_helper.py test

# Open lab guide and start Module 1
```

---

## 📚 Lab Modules Overview

### Module 1: Model Selection (30 min)
**What You'll Learn:**
- How to request and enable model access
- Compare different foundation models
- Understand model performance tradeoffs
- Use playground and programmatic testing

**Key Exercises:**
- Enable 5+ foundation models
- Test Claude, Llama, and Titan models
- Compare latency, quality, and cost
- Write comparison script

**Deliverables:**
- Working model comparison script
- Performance benchmark results
- Decision matrix for model selection

---

### Module 2: Prompt Management (45 min)
**What You'll Learn:**
- Advanced prompt engineering techniques
- Create and version prompt templates
- Use Bedrock Prompt Management
- Optimize prompts for best results

**Key Exercises:**
- Test zero-shot, few-shot, and chain-of-thought prompting
- Create customer service prompt template
- Implement prompt versioning
- Build reusable prompt library

**Deliverables:**
- Customer service template
- Multiple prompt versions
- Python prompt management code

---

### Module 3: Knowledge Bases (60 min)
**What You'll Learn:**
- Implement Retrieval Augmented Generation (RAG)
- Create and configure Knowledge Bases
- Query with semantic search
- Apply metadata filtering

**Key Exercises:**
- Prepare and upload documents to S3
- Create Knowledge Base with vector store
- Test queries with different prompts
- Implement metadata filtering
- Query programmatically with Python

**Deliverables:**
- Fully functional Knowledge Base
- Sample documents indexed
- Query testing results
- Python integration code

---

### Module 4: Guardrails (45 min)
**What You'll Learn:**
- Configure content filters and safety controls
- Set up denied topics and word filters
- Implement PII detection and redaction
- Use automated reasoning for accuracy

**Key Exercises:**
- Create comprehensive guardrail
- Configure 5 protection policies
- Test with harmful and safe content
- Apply guardrails to Knowledge Base
- Implement automated reasoning checks

**Deliverables:**
- Production-ready guardrail
- Test cases and results
- PII filtering demonstration
- Integration with KB

---

### Module 5: Model Fine-Tuning (60 min)
**What You'll Learn:**
- Prepare training data in JSONL format
- Configure and launch fine-tuning jobs
- Evaluate fine-tuned model performance
- Use provisioned throughput

**Key Exercises:**
- Create 20+ training examples
- Launch fine-tuning job
- Compare base vs fine-tuned model
- Test on validation set
- Purchase provisioned throughput

**Deliverables:**
- Fine-tuned model for sentiment analysis
- Training and validation datasets
- Performance comparison results
- Provisioned throughput setup

---

### Module 6: Data Automation (30 min)
**What You'll Learn:**
- Extract structured data from documents
- Process invoices, resumes, and forms
- Batch document processing
- Validate extracted data

**Key Exercises:**
- Create sample invoices and resumes
- Extract JSON from unstructured text
- Batch process multiple documents
- Implement validation schemas
- Handle errors gracefully

**Deliverables:**
- Document processing pipeline
- Structured data extraction
- Batch processing script
- Validation framework

---

### Module 7: Model Evaluation (45 min)
**What You'll Learn:**
- Create evaluation datasets
- Run systematic model comparisons
- Define custom metrics
- Implement A/B testing

**Key Exercises:**
- Prepare 10+ test cases
- Run automated evaluations
- Calculate accuracy, latency, quality
- Compare multiple models
- Create evaluation visualizations
- Set up A/B testing framework

**Deliverables:**
- Evaluation dataset
- Model comparison report
- Custom metrics implementation
- A/B testing framework
- Visualization charts

---

### Module 8: End-to-End Application (30 min)
**What You'll Learn:**
- Integrate all Bedrock features
- Build production-ready chatbot
- Handle conversation history
- Implement error handling

**Key Exercises:**
- Build customer service bot
- Integrate KB, Guardrails, and Agents
- Track conversation context
- Generate conversation summaries
- Deploy complete application

**Deliverables:**
- Full-featured chatbot application
- Conversation management
- Error handling
- Production deployment code

---

## 💡 What Makes This Lab Unique

### Comprehensive Coverage
- **All major features** covered in one lab
- **Real-world scenarios** not just theory
- **Production-ready code** you can use immediately
- **Best practices** from AWS experts

### Hands-On Learning
- **80% practical exercises** vs 20% theory
- **Working code examples** for every concept
- **Troubleshooting guides** for common issues
- **Progressive difficulty** building on previous modules

### Production Focus
- **Enterprise patterns** and architectures
- **Security and compliance** considerations
- **Cost optimization** strategies
- **Monitoring and evaluation** frameworks

### Complete Automation
- **One-command setup** gets you started fast
- **Helper scripts** for common tasks
- **Configuration management** made easy
- **Cleanup automation** to avoid charges

---

## 🎯 Learning Outcomes

By completing this lab, you will be able to:

### Technical Skills
✅ Select appropriate models for different use cases  
✅ Engineer effective prompts for optimal results  
✅ Build RAG applications with Knowledge Bases  
✅ Implement comprehensive safety guardrails  
✅ Fine-tune models with custom data  
✅ Extract structured data from documents  
✅ Evaluate and compare model performance  
✅ Deploy production-ready AI applications

### Business Value
✅ Reduce development time by 50%+  
✅ Implement enterprise AI safely and compliantly  
✅ Optimize costs through smart model selection  
✅ Build customer-facing AI applications  
✅ Automate document processing workflows  
✅ Ensure AI accuracy and reliability

### Career Growth
✅ AWS Bedrock expertise (high-demand skill)  
✅ Practical AI/ML implementation experience  
✅ Portfolio projects for interviews  
✅ Foundation for AWS ML certifications

---

## 📊 Lab Statistics

### Code Examples
- **500+ lines** of Python code
- **20+ complete** working examples
- **50+ API calls** demonstrated
- **10+ integration** patterns

### Exercises
- **40+ hands-on** exercises
- **8 major projects** (one per module)
- **100+ test cases** to validate learning

### Documentation
- **10,000+ words** of detailed instructions
- **Architecture diagrams** included
- **Troubleshooting guides** for common issues
- **Best practices** throughout

---

## 💰 Cost Breakdown

### Estimated Costs (with cleanup)
- **Model Inference:** $2-5
- **Knowledge Base:** $1-2
- **Fine-Tuning:** $3-8
- **Guardrails:** $1-2
- **Storage (S3):** <$1
- **OpenSearch:** $2-5
- **Total:** ~$10-25

### Cost Optimization Tips
✅ Complete lab in one session  
✅ Use Haiku for testing  
✅ Delete resources immediately after  
✅ Use batch inference (50% discount)  
✅ Monitor usage with CloudWatch

### Zero-Cost Options
- Many exercises work with free tier
- Use playgrounds instead of API calls
- Skip fine-tuning module (optional)
- Use smaller datasets

---

## 🛠️ Technical Requirements

### AWS Services Used
- Amazon Bedrock (Foundation Models)
- Amazon S3 (Storage)
- Amazon OpenSearch Serverless (Vector DB)
- AWS IAM (Permissions)
- AWS CloudWatch (Monitoring)

### Local Requirements
- **Operating System:** Linux, macOS, or Windows (WSL)
- **Python:** 3.8 or higher
- **Disk Space:** 1GB free
- **Internet:** Stable connection required
- **Browser:** Modern browser for AWS Console

### AWS Permissions Required
- `bedrock:*` (full Bedrock access)
- `s3:*` (bucket operations)
- `iam:*` (role management)
- `aoss:*` (OpenSearch Serverless)
- `logs:*` (CloudWatch logs)

---

## 📖 How to Use This Lab

### Self-Paced Learning
1. **Set aside 3-4 hours** of uninterrupted time
2. **Run setup script** to prepare environment
3. **Complete modules sequentially** (they build on each other)
4. **Practice each exercise** before moving forward
5. **Take notes** on learnings and challenges
6. **Clean up resources** when finished

### Team Training
1. **Assign pre-work:** Review prerequisites
2. **Live demo:** Instructor demonstrates setup
3. **Pair programming:** Teams work through modules
4. **Code review:** Share solutions and discuss
5. **Q&A session:** Address questions and troubleshooting
6. **Retrospective:** Discuss learnings and applications

### Certification Prep
1. **Complete all modules** for comprehensive coverage
2. **Review best practices** sections carefully
3. **Practice troubleshooting** common issues
4. **Build portfolio project** using learned skills
5. **Take practice quizzes** (create based on content)

---

## 🆘 Getting Help

### During the Lab
- **Quick Reference:** Check `quick_reference.md`
- **Troubleshooting:** Each module has common issues section
- **Helper Script:** Use `bedrock_helper.py` commands
- **AWS Docs:** Links provided throughout

### After the Lab
- **AWS re:Post:** Community Q&A forum
- **AWS Support:** If you have a support plan
- **GitHub Issues:** Report problems with lab materials
- **AWS Workshops:** Additional hands-on content

---

## 🎓 Next Steps After Completion

### Continue Learning
1. **AWS Bedrock Workshop:** catalog.workshops.aws/amazon-bedrock
2. **Build Your Own Project:** Apply to real use case
3. **Explore Advanced Features:** Agents, Flows, Custom Models
4. **AWS Certifications:** ML Specialty, Solutions Architect

### Share Your Success
1. **Blog about your experience**
2. **Share on LinkedIn**
3. **Present at meetups**
4. **Contribute improvements** to lab materials

### Production Deployment
1. **Review security best practices**
2. **Implement monitoring and logging**
3. **Set up CI/CD pipelines**
4. **Plan for scaling and optimization**

---

## 📝 Feedback and Contributions

We value your feedback to improve this lab!

### How to Provide Feedback
- **What worked well?** Share your wins
- **What was confusing?** Help us clarify
- **What's missing?** Suggest additions
- **Found bugs?** Report issues

### How to Contribute
- **Fix typos or errors**
- **Add additional examples**
- **Improve documentation**
- **Translate to other languages**

---

## 📄 License and Usage

This lab is provided for educational purposes. You are free to:
- ✅ Use for personal learning
- ✅ Use for team training
- ✅ Modify for your needs
- ✅ Share with attribution

Please note:
- ❌ Do not sell or commercialize
- ❌ AWS charges apply for resources used
- ❌ No warranty or support guaranteed

---

## 🏆 Completion Certificate

Upon completing all 8 modules:

1. **Document your work:**
   - Screenshots of completed exercises
   - Working code repositories
   - Evaluation results

2. **Build portfolio project:**
   - Use case description
   - Architecture diagram
   - Demo video or screenshots

3. **Share your achievement:**
   - LinkedIn post with #AWSBedrock
   - Blog post about experience
   - GitHub repository with code

---

## 📞 Contact and Support

### Lab Authors
- Created for AWS Bedrock learners worldwide
- Updated regularly with latest features
- Community-driven improvements

### Stay Updated
- Watch for new modules and exercises
- Follow AWS announcements for new features
- Join AWS community forums

---

**Version:** 1.0  
**Last Updated:** November 2024  
**Tested With:** Claude 3.5 Sonnet, Claude 3 Haiku, Llama 3.2

---

## ✅ Ready to Start?

1. **Read through this overview**
2. **Ensure prerequisites are met**
3. **Run `./setup_lab.sh`**
4. **Open `bedrock_lab.md`**
5. **Begin Module 1!**

**Good luck and happy learning! 🚀**
