"""
data_loader.py - Dataset Loading & Preparation
Fake News Detector Project
"""

import pandas as pd


class DataLoader:
    """
    Loads news datasets from CSV files with automatic column detection.
    Falls back to a built-in sample dataset if no file is found.
    """

    # Priority-ordered candidate names for text and label columns
    TEXT_COLUMN_CANDIDATES = ['text', 'title', 'content', 'news', 'article', 'headline', 'body']
    LABEL_COLUMN_CANDIDATES = ['label', 'class', 'fake', 'target', 'category']

    def load_dataset(self, filepath: str) -> pd.DataFrame:
        """
        Load and preprocess a news dataset from a CSV file.

        Args:
            filepath: Path to the CSV file.

        Returns:
            Cleaned DataFrame with 'text' and 'label' columns.
            Label: 0 = Real, 1 = Fake.
        """
        try:
            df = pd.read_csv(filepath, encoding='utf-8')
        except FileNotFoundError:
            print(f"  [!] Dataset file '{filepath}' not found. Using built-in sample dataset.")
            return self.create_fallback_dataset()
        except Exception as exc:
            print(f"  [!] Failed to read '{filepath}': {exc}. Using built-in sample dataset.")
            return self.create_fallback_dataset()

        # Detect columns
        text_col = self._detect_column(df, self.TEXT_COLUMN_CANDIDATES)
        label_col = self._detect_column(df, self.LABEL_COLUMN_CANDIDATES)

        if text_col is None or label_col is None:
            print("  [!] Could not auto-detect required columns. Using built-in sample dataset.")
            return self.create_fallback_dataset()

        # Normalize column names
        df = df[[text_col, label_col]].copy()
        df.columns = ['text', 'label']

        # Map labels to 0 (Real) / 1 (Fake)
        df['label'] = df['label'].apply(self._normalize_label)

        # Drop rows with missing or invalid values
        df = df.dropna(subset=['text', 'label'])
        df = df[df['text'].astype(str).str.strip() != '']
        df['label'] = df['label'].astype(int)

        print(f"  [OK] Dataset loaded: {len(df)} articles "
              f"({(df['label'] == 0).sum()} real, {(df['label'] == 1).sum()} fake)")

        return df.reset_index(drop=True)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _detect_column(self, df: pd.DataFrame, candidates: list) -> str | None:
        """Return the first candidate column name found in the DataFrame."""
        lower_cols = {c.lower(): c for c in df.columns}
        for candidate in candidates:
            if candidate.lower() in lower_cols:
                return lower_cols[candidate.lower()]
        return None

    @staticmethod
    def _normalize_label(value) -> float | None:
        """
        Map diverse label formats to binary 0 / 1.
        Returns None for unrecognized values (will be dropped).
        """
        mapping = {
            # numeric
            0: 0, 1: 1, '0': 0, '1': 1,
            # text
            'real': 0, 'true': 0, 'no': 0, 'legit': 0,
            'fake': 1, 'false': 1, 'yes': 1, 'hoax': 1,
        }
        if isinstance(value, str):
            value = value.strip().lower()
        return mapping.get(value, None)

    # ------------------------------------------------------------------
    # Fallback dataset
    # ------------------------------------------------------------------

    def create_fallback_dataset(self) -> pd.DataFrame:
        """
        Create a small, balanced sample dataset for demonstration and testing.
        Contains 60 real and 60 fake news examples.
        """
        real_news = [
            "The Federal Reserve announced a quarter-point interest rate hike citing persistent inflation concerns and a resilient labor market.",
            "Scientists at MIT have developed a new battery technology that could double the range of electric vehicles while cutting charging time significantly.",
            "The United Nations Security Council passed a resolution calling for an immediate ceasefire in the ongoing regional conflict.",
            "NASA's James Webb Space Telescope captured unprecedented images of a galaxy cluster 4.6 billion light-years away.",
            "Apple reported record quarterly earnings driven by strong iPhone and services revenue growth across emerging markets.",
            "The World Health Organization issued updated guidelines on sugar intake recommending adults consume no more than 25 grams daily.",
            "SpaceX successfully launched 60 Starlink satellites into low Earth orbit, expanding broadband coverage across rural areas.",
            "Researchers at Oxford University published a peer-reviewed study linking regular exercise to reduced risk of cognitive decline in older adults.",
            "The European Central Bank raised its key interest rates for the sixth consecutive meeting as inflation remains above target.",
            "Amazon announced plans to hire 100,000 warehouse workers ahead of the holiday shopping season to meet growing demand.",
            "The Supreme Court ruled 6-3 in favor of stricter environmental regulations on industrial emissions near waterways.",
            "Global temperatures in 2024 set a new record, surpassing the previous high by 0.3 degrees Celsius according to NOAA data.",
            "The International Monetary Fund revised its global growth forecast upward to 3.2 percent for the current fiscal year.",
            "Microsoft completed its $68.7 billion acquisition of Activision Blizzard after receiving final regulatory clearances worldwide.",
            "A clinical trial published in The Lancet showed a new malaria vaccine achieving 77 percent efficacy in children.",
            "The US Treasury Department sanctioned several entities linked to cyber attacks on critical financial infrastructure.",
            "Economists warn that high borrowing costs and tight credit conditions could push several advanced economies into recession.",
            "The Paris Agreement signatories met to review progress and recommit to updated nationally determined contributions.",
            "Samsung unveiled its next-generation foldable smartphone featuring an under-display camera and enhanced hinge durability.",
            "The Centers for Disease Control and Prevention updated its vaccination schedule to include updated formulations for fall.",
            "Oil prices fell sharply after OPEC announced it would maintain current production levels despite market pressure to cut.",
            "Scientists discovered a new species of deep-sea fish exhibiting bioluminescence patterns not previously observed in vertebrates.",
            "The Bank of England kept interest rates on hold as inflation showed signs of easing toward the 2 percent target.",
            "A landmark climate bill passed the Senate, committing $500 billion over ten years to clean energy infrastructure.",
            "Google launched its next generation of AI language models, outperforming competitors on multiple standardized benchmarks.",
            "Researchers found strong evidence that a Mediterranean diet reduces the risk of heart disease by up to 30 percent.",
            "The unemployment rate fell to its lowest level in 54 years as job growth exceeded economists' expectations last month.",
            "Tesla expanded its Supercharger network by 20 percent in the second quarter, adding thousands of new charging stalls.",
            "The International Space Station celebrated its 25th anniversary of continuous human habitation in orbit.",
            "A new study in Nature Medicine found that a simple blood test can detect multiple cancers up to four years early.",
            "The US Federal Aviation Administration approved new air traffic management rules designed to reduce flight delays.",
            "Amazon Web Services reported a 37 percent revenue increase in cloud computing as enterprise migration accelerated.",
            "The World Trade Organization ruled against tariffs on solar panel imports, citing violations of international trade law.",
            "Scientists confirmed that the Antarctic ice sheet is losing mass at an accelerating rate due to warming ocean currents.",
            "The Dow Jones Industrial Average closed at a record high driven by strong earnings in the technology and healthcare sectors.",
            "Pharmaceutical giant Pfizer received FDA approval for a new treatment targeting treatment-resistant depression.",
            "The G20 summit concluded with a joint declaration pledging cooperation on debt relief for developing nations.",
            "A study published in JAMA found that telemedicine improves health outcomes in rural populations with limited clinic access.",
            "California enacted a landmark data privacy law giving residents greater control over how companies use personal information.",
            "Meta reported strong advertising revenue growth despite regulatory challenges in Europe and increased competition.",
            "Scientists using CRISPR technology successfully corrected a genetic mutation responsible for sickle cell disease in patients.",
            "The US Department of Energy announced $7 billion in grants for clean hydrogen production and storage facilities.",
            "China's GDP grew at 5.1 percent in the last quarter, slightly above government targets and analysts' expectations.",
            "Twitter's algorithm was found to amplify political content disproportionately according to an independent audit published today.",
            "The FDA approved the first over-the-counter hearing aid, making hearing assistance accessible to millions of Americans.",
            "A record 2.3 million electric vehicles were sold globally in the first quarter, representing a 35 percent year-over-year increase.",
            "New research shows that deep sleep is critical for clearing toxic proteins from the brain associated with Alzheimer's disease.",
            "The European Union introduced new regulations requiring large platforms to audit and reduce algorithmic content amplification.",
            "Inflation in the eurozone fell to 2.4 percent in March, the lowest level since the energy price shock of 2021.",
            "Scientists successfully tested a quantum computing algorithm capable of breaking current RSA encryption standards in theory.",
            "The World Bank approved a $3 billion climate resilience package for vulnerable island nations facing sea-level rise.",
            "Researchers developed an AI model that can predict hospital readmissions with 90 percent accuracy using electronic records.",
            "The US housing market showed signs of recovery as mortgage rates declined and new home sales exceeded forecasts.",
            "A coalition of nations pledged to phase out coal power by 2035 at the annual international climate summit.",
            "Amazon's Alexa now supports real-time translation across 30 language pairs, enabling global voice assistant usage.",
            "The Nobel Prize in Physics was awarded for groundbreaking work on attosecond laser pulses and electron dynamics.",
            "Genetic research confirmed that modern humans and Neanderthals interbred multiple times across different regions of Europe.",
            "OpenAI released a new safety framework for large language models outlining responsible deployment guidelines for enterprises.",
            "The International Renewable Energy Agency reports solar power is now the cheapest electricity source in history.",
            "Health authorities confirmed that childhood vaccination rates have recovered to pre-pandemic levels in most developed nations.",
        ]

        fake_news = [
            "BREAKING: Scientists discover miracle cure for all diseases hidden by pharmaceutical companies for decades!",
            "SHOCKING: The moon landing was staged in a Hollywood studio and NASA has finally admitted the truth.",
            "You won't believe what they put in tap water to control the population! Secret government program exposed!",
            "5G towers are actually mind control devices installed under cover of COVID lockdowns according to leaked documents.",
            "Billionaires are meeting secretly to reduce world population by 90 percent through vaccines and chemtrails.",
            "Ancient pyramids were built by aliens and the Egyptian government has been hiding the evidence for 50 years.",
            "World's largest gold deposit discovered beneath the Vatican proving the church has been hiding global wealth.",
            "Celebrity doctors reveal the one vegetable that cures cancer doctors don't want you to know about.",
            "Time traveler from 2075 warns of imminent global disaster caused by secret AI program activated last Tuesday.",
            "Government chemtrails confirmed to contain mind-altering chemicals to keep citizens docile and obedient.",
            "EXPOSED: Your smart TV is secretly recording every conversation and streaming it to intelligence agencies in real time.",
            "Miracle seed oil discovered in the Amazon jungle permanently reverses diabetes in just three days without medication.",
            "World leaders are reptilian shapeshifters according to classified documents leaked by insider whistleblower.",
            "Banks preparing to freeze all accounts this weekend to introduce forced digital currency and end paper money forever.",
            "ALERT: New law secretly passed allowing the government to arrest citizens for thinking negative thoughts about officials.",
            "Doctors are paid to inject cancer cells into patients disguised as flu shots to boost hospital revenue.",
            "Hidden cave beneath Antarctica contains live dinosaurs kept secret by a global scientific conspiracy since 1947.",
            "Drinking bleach mixed with lemon juice kills COVID-19 virus in minutes according to suppressed Harvard study.",
            "NASA admits it has been communicating with alien civilizations for 30 years but kept it classified until now.",
            "The Great Wall of China is actually a giant solar energy collector built by an ancient advanced civilization.",
            "BREAKING: Elite global cabal harvesting children's blood to extend their own lives exposed by undercover journalist.",
            "Microchips in vaccines are being activated by 5G signals to steal passwords and bank account information.",
            "Secret underground bunkers being built for the elite while the public is told climate change is a hoax.",
            "This simple lemon and baking soda recipe dissolves tumors overnight and is being suppressed by Big Pharma.",
            "Military whistleblower reveals the government has time travel technology and has visited the future multiple times.",
            "Scientists are not actually studying climate change but are weather engineers controlling rain and drought for profit.",
            "Ancient manuscripts found proving Jesus was actually an extraterrestrial sent to prepare humanity for alien contact.",
            "Banks will collapse next month according to top insider who fled to safety with evidence of the coming crash.",
            "All major world leaders are controlled by a secret society that has run the planet for 2,000 years in secret.",
            "Eating only raw food and magnets aligned north can cure Parkinson's disease better than any medication available.",
            "CONFIRMED: Mainstream media has been scripted by a single corporation that controls all news broadcasts globally.",
            "Drinking silver water eliminates all autoimmune diseases and has been kept off the market by pharmaceutical firms.",
            "A whistleblower revealed that social media platforms are legally required to share all private messages with the CIA.",
            "SHOCKING VIDEO: Politician caught on tape admitting the official COVID death numbers are fabricated by ten times.",
            "Scientists discover that the earth is actually hollow with an entire civilization living inside the planet's core.",
            "New study proves that fluoride in water reduces IQ by 25 points and is being used to dumb down the population.",
            "George Soros secretly funded the entire election to install puppets in government at every level confirmed by insider.",
            "You can increase your IQ by 50 points in one week using this ancient breathing technique banned by western doctors.",
            "Banned documentary reveals how hospitals are paid to falsify death certificates to artificially inflate COVID numbers.",
            "The pharmaceutical industry engineered COVID-19 in a lab to sell vaccines and make trillions in guaranteed profits.",
            "World's most powerful families are secretly planning to eliminate cash and force a mark on every human by 2025.",
            "Scientists have proven that the earth is stationary and all space exploration footage is entirely computer generated.",
            "This one weird trick doctors discovered makes cancer disappear but the treatment was banned to protect drug profits.",
            "Climate change is an elaborate hoax invented by globalists to impose carbon taxes and seize control of economies.",
            "Former president secretly arrested at 3am and replaced by an actor according to credible military intelligence source.",
            "Honey mixed with turmeric and black pepper cures HIV/AIDS better than any antiretroviral therapy available today.",
            "Secret space program has been operating for 60 years using alien technology recovered from crash sites worldwide.",
            "EXPOSED: Hospitals are injecting patients with lethal doses of medication and reporting them as natural COVID deaths.",
            "Mysterious disease killing thousands is being caused by 5G activation and the media is completely covering it up.",
            "Scientists confirmed water has memory and can be programmed to heal disease using positive thoughts and intention.",
            "This ancient remedy suppressed by big pharma since the 1940s cures all forms of cancer in less than a week.",
            "World Economic Forum member accidentally confirmed on hot mic that COVID was engineered to trigger global reset.",
            "Crystals charged under a full moon can replace insulin for diabetics if held against the pancreas during meditation.",
            "Military satellites are targeting and killing dissidents worldwide using directed energy beams from low Earth orbit.",
            "The moon is actually an artificial satellite placed in orbit by advanced aliens to monitor Earth's development.",
            "Doctors admitting secretly that aspirin mixed with household bleach is a powerful cure for all cancers if taken daily.",
            "Planetary alignment happening next month will cause massive earthquakes and governments are hiding evacuation plans.",
            "Shadow government operation revealed by insider showing all terrorist attacks in the past decade were staged events.",
            "Oil companies have suppressed free energy technology for 100 years to maintain control of global fuel markets.",
            "Scientists stunned as man regrows severed limb in 30 days using suppressed stem cell technique developed in 1960s.",
        ]

        texts = real_news + fake_news
        labels = [0] * len(real_news) + [1] * len(fake_news)

        df = pd.DataFrame({'text': texts, 'label': labels})
        print(f"  [OK] Built-in sample dataset created: {len(df)} articles "
              f"({len(real_news)} real, {len(fake_news)} fake)")
        return df
