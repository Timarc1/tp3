# ---------------------------------------------------
# ---------- Classes utilisées sur le site ----------
# ---------------------------------------------------
class Definition:
    def __init__(self, terme, texte, source):
        self.terme = terme
        self.texte = texte
        self.source = source

    def termes_relies(self):
        # TODO : passer à travers tous les termes définis dans le
        # tableau `glossaire` et retourner un tableau de termes qui
        # sont présents dans le texte
        termes = []
        for definition in glossaire:
            if definition.terme in self.texte:
                termes.append(definition.terme)
        return termes
        

        #return []


class Article:
    numero = 0

    def __init__(self, titre, date, texte, image):
        self.titre = titre
        self.date = date
        self.texte = texte
        self.image = image

        self.numero = Article.numero
        Article.numero += 1

    def tableau_paragraphes(self):
        return self.texte.split('\n\n')

    def temps_lecture(self):
        """Calcule le nombre de mot et donne une estimation
        du nombre de temps pour lire l<article"""
        nbr_mots = len(self.texte.split(" "))
        temps = round(nbr_mots / 200, 2)
        return temps


class Ordinateur:
    def __init__(self):
        self.composantes = []

    def sous_total(self):
        # TODO
        print("TODO: calculer le sous-total en additionnant le prix de toutes les composantes")
        prix_total = 0
        for composante in self.composantes:
            prix_total += composante.prix
        return prix_total


    def taxes(self):
        """Calcule les taxes """
        
        taxe = 0.15 * self.sous_total()
        return taxe


    def total(self):
        """Calcule le montant avec taxes """
        total = self.sous_total() + self.taxes()
        return total


class Composante():
    def __init__(self, description, prix, lien):
        self.description = description
        self.lien = lien
        self.prix = prix


# ---------------------------------------------------
# ---------- Données à utiliser sur le site ---------
# ---------------------------------------------------

# Variables :
# glossaire (tableau d'objets Definition)
# articles (tableau d'objets Article)
# composantes (*dictionnaire* 'type' => [tableau de choix d'objets Composante])

glossaire = [
    Definition('case',
        """A computer case, also known as a computer chassis, is the enclosure that contains most of the components of a personal computer (usually excluding the display, keyboard, and mouse). Cases are usually constructed from steel (often SECC—steel, electrogalvanized, cold-rolled, coil), aluminium and plastic. Other materials such as glass, wood, acrylic and even Lego bricks have appeared in home-built cases.""", 'https://en.wikipedia.org/wiki/Computer_case'),
    Definition('motherboard', """A motherboard (also called mainboard, main circuit board, mb, mboard, backplane board, base board, system board, logic board (only in Apple computers) or mobo) is the main printed circuit board (PCB) in general-purpose computers and other expandable systems. It holds and allows communication between many of the crucial electronic components of a system, such as the central processing unit (CPU) and memory, and provides connectors for other peripherals. Unlike a backplane, a motherboard usually contains significant sub-systems, such as the central processor, the chipset's input/output and memory controllers, interface connectors, and other components integrated for general use.

Motherboard means specifically a PCB with expansion capabilities. As the name suggests, this board is often referred to as the "mother" of all components attached to it, which often include peripherals, interface cards, and daughterboards: sound cards, video cards, network cards, host bus adapters, TV tuner cards, IEEE 1394 cards; and a variety of other custom components.""", 'https://en.wikipedia.org/wiki/Motherboard'),
    Definition('cpu', """A central processing unit (CPU), also called a central processor, main processor or just processor, is the electronic circuitry that executes instructions comprising a computer program. The CPU performs basic arithmetic, logic, controlling, and input/output (I/O) operations specified by the instructions in the program. This contrasts with external components such as main memory and I/O circuitry, and specialized processors such as graphics processing units (GPUs).

The form, design, and implementation of CPUs have changed over time, but their fundamental operation remains almost unchanged. Principal components of a CPU include the arithmetic–logic unit (ALU) that performs arithmetic and logic operations, processor registers that supply operands to the ALU and store the results of ALU operations, and a control unit that orchestrates the fetching (from memory), decoding and execution (of instructions) by directing the coordinated operations of the ALU, registers and other components.

Most modern CPUs are implemented on integrated circuit (IC) microprocessors, with one or more CPUs on a single IC chip. Microprocessor chips with multiple CPUs are multi-core processors. The individual physical CPUs, processor cores, can also be multithreaded to create additional virtual or logical CPUs.

An IC that contains a CPU may also contain memory, peripheral interfaces, and other components of a computer; such integrated devices are variously called microcontrollers or systems on a chip (SoC).""",
'https://en.wikipedia.org/wiki/Central_processing_unit'),
    Definition('storage', """Long-term storage like operating system, software programs, and
personal files. Size determined by megabytes (MB), gigabytes (GB), and
terabytes (TB).""", 'https://checkify.com/daily-checklists/build-your-own-pc-checklist/'),
    Definition('cooling', """Fans / CPU Cooler dissipates the hot air from the computer. CPU fan
or water cooling? This is down to personal preference.""", 'https://checkify.com/daily-checklists/build-your-own-pc-checklist/'),
    Definition('ram', """Random Access Memory. Temporary, short-term storage of information for rapid retrieval
without it a computer can’t perform simple tasks.""", 'https://checkify.com/daily-checklists/build-your-own-pc-checklist/'),
    Definition('power', """PSU (Power Supply Unit) converts power from the wall socket which
is alternating current AC to low-voltage regulated DC power that your
motherboard and processor needs. Decide on the other components first
so you know what power supply will need. Calculating how much power
you need in watts. Add all the components power consumption together
and add an additional 20% and that is the amount of wattage you
need.""", 'https://checkify.com/daily-checklists/build-your-own-pc-checklist/'),
    Definition('keyboard', """A computer keyboard is a peripheral input device modeled after the typewriter keyboard which uses an arrangement of buttons or keys to act as mechanical levers or electronic switches. Replacing early punched cards and paper tape technology, interaction via teleprinter-style keyboards have been the main input method for computers since the 1970s, supplemented by the computer mouse since the 1980s.

Keyboard keys (buttons) typically have a set of characters engraved or printed on them, and each press of a key typically corresponds to a single written symbol. However, producing some symbols may require pressing and holding several keys simultaneously or in sequence. While most keys produce characters (letters, numbers or symbols), other keys (such as the escape key) can prompt the computer to execute system commands. In a modern computer, the interpretation of key presses is generally left to the software: the information sent to the computer, the scan code, tells it only which physical key (or keys) was pressed or released.

In normal usage, the keyboard is used as a text entry interface for typing text, numbers, and symbols into application software such as a word processor, web browser or social media app.""", "https://en.wikipedia.org/wiki/Computer_keyboard"),
    Definition('mouse', """A computer mouse is a hand-held pointing device that detects
two-dimensional motion relative to a surface. This motion is typically
translated into the motion of a pointer on a display, which allows a
smooth control of the graphical user interface of a computer. """, "https://en.wikipedia.org/wiki/Computer_mouse"),
    Definition('network', """Ethernet card. Transmit data from the network to your computer. Some of these cards can include WIFI""",'https://checkify.com/daily-checklists/build-your-own-pc-checklist/'),
    Definition('sound', """Sound Cards. Allow the use of audio components.""",'https://checkify.com/daily-checklists/build-your-own-pc-checklist/'),
    Definition('gpu', """Graphical process unit. Helps processing images before rendering them on the monitor.""",'https://checkify.com/daily-checklists/build-your-own-pc-checklist/'),
    Definition('monitor', """A computer monitor is an output device that displays information in pictorial or text form. A monitor usually comprises a visual display, some circuitry, a casing, and a power supply. The display device in modern monitors is typically a thin-film-transistor liquid-crystal display (TFT-LCD) with LED backlighting having replaced cold-cathode fluorescent lamp (CCFL) backlighting. Previous monitors used a cathode-ray tube (CRT) and some plasma (also called gas-plasma) displays. Monitors are connected to the computer via VGA, Digital Visual Interface (DVI), HDMI, DisplayPort, USB-C, low-voltage differential signaling (LVDS) or other proprietary connectors and signals. """, "https://en.wikipedia.org/wiki/Computer_monitor"),
]



articles = [
    Article("Bienvenue!", "15 août 2022", """Le site OrdinaLand ouvre officiellement ses portes!

Venez profiter de notre Glossaire, venez consulter notre Blog, et
surtout, profitez de notre super outil gratuit d'aide à la
construction d'un ordinateur!
""", "penguin.png"),


    Article("Promotion d'ouverture!", "15 août 2022", """Nouvelle promotion sur le site!
Entrez le code BIENVENUE pour profiter d'un rabais de 15%!
""", "discount.png"),


    Article("Tout savoir sur les souris", "16 août 2022", """Non nihil quasi odit aut aut voluptatibus id. Mollitia consequatur eos excepturi provident doloremque fugit. Dolorem nisi est cum possimus. Aut quasi rerum necessitatibus. Corrupti aut quidem facilis omnis labore atque. Temporibus rerum doloremque sed et expedita.

Commodi voluptatem consequatur ea. Et ad maxime molestiae rerum. Repudiandae et reprehenderit a placeat velit officia hic voluptatem.

Explicabo iste maiores repudiandae dolorem. Facilis dolore aperiam sequi impedit praesentium est. Accusamus tenetur velit quam quo quas nisi. Earum facilis enim ipsum excepturi. In in odio ipsum nisi dolor aperiam.

Assumenda vitae animi deleniti accusantium. Excepturi dolore sequi odit. Corrupti aut pariatur dolorem nesciunt consequatur quae animi. Ut distinctio repudiandae quia. Assumenda distinctio dolor non quia aliquid voluptatem. Dolorem dicta minus inventore id quasi.

Ullam non modi accusamus repellat numquam dolorem. Eos a culpa corrupti ad ipsam excepturi numquam. Voluptatem quis assumenda voluptatem eveniet cum error omnis. Accusantium blanditiis et sint sint velit sint expedita. Animi aliquid natus odit non non voluptatem neque reprehenderit. Amet et eum rerum non modi cum.

""", "mouse.png"),

    Article("Promotion", "16 août 2022", """Nouvelle promotion sur le site!
Entrez le code TWADO pour profiter d'un rabais de 25%!
""", "discount.png"),

    Article("Vous avez des questions?", "16 août 2022", """N'hésitez pas à faire un tour sur notre page Contact!

Nous garderons à jour nos horaires d'ouverture et notre adresse. Pour toute question, venez nous dire un petit coucou en personne!

C'est la fin de cet article. Voici un peu de Lorem Ipsum pour le rendre plus long :



Est ipsa odit fugit officia ipsum impedit nobis. Ut nemo atque praesentium ea est perferendis. Veniam aut qui labore nihil. Placeat odio aliquam animi labore exercitationem.

Qui minima tenetur consectetur ipsa magni quia autem ab. Nemo sint maiores sapiente porro eum cum. Excepturi qui natus aut. Velit voluptate autem sapiente labore. Molestias quo fuga sed id. Quasi enim consectetur est.

Excepturi ea voluptatum quis autem ea est ea. Iure impedit sequi eligendi dolores. Alias sit laudantium et nostrum iste tempora. Ullam dolorum molestias est iure vel.

Qui temporibus et aliquam et modi saepe et. Nostrum sed magnam alias ipsa qui accusantium hic alias. Ipsum repellendus ullam autem. Repudiandae quos id quo id est aut. Ea ex dolorem necessitatibus in.

Ab sequi molestiae laborum quasi dicta delectus animi qui. Minus repellendus odit est non. Qui fugit excepturi illum itaque in enim rerum. Enim commodi pariatur et similique quibusdam quas. Explicabo aliquid cupiditate ad.

Voluptates nam itaque tempore cum. Quia amet laboriosam error expedita rem vel consectetur. Voluptatem enim earum beatae modi error et itaque. Quibusdam autem molestias inventore. Deserunt est voluptates voluptatum rem eum et eaque. Repellat velit autem deserunt quisquam adipisci ut omnis modi.

Dolor quasi eius quae aut ratione nostrum ratione porro. Ut omnis facilis blanditiis beatae eligendi fugit. Deleniti consequatur ut voluptatem. Ea deleniti sunt quis.

Dolor quasi sit atque explicabo impedit. Fuga dolores ex soluta. Corrupti aut ipsa ab aut ipsum veritatis enim aspernatur. Ullam sit sint suscipit cumque est exercitationem.

Ea aut voluptate a ipsum molestiae pariatur. Non ex veniam ea. Culpa est odio vel beatae ut.

Autem dignissimos esse mollitia eius voluptatem sit cum. Vero alias temporibus blanditiis optio maiores voluptatem natus provident. Repudiandae sint amet officia nesciunt. Reiciendis eligendi sed veniam repudiandae odit accusantium. Aut nobis quia quia dolorem animi perferendis.""", "question.png"),

    Article("Promotion", "18 août 2022", """Nouvelle promotion sur le site!
Entrez le code PROMO55 pour profiter d'un rabais de 55%!
""", "discount.png"),

    Article("Tout savoir sur la RAM", "16 août 2022", """Article tiré de Wikipédia (https://fr.wikipedia.org/wiki/M%C3%A9moire_vive)

La mémoire vive, parfois abrégée avec l'acronyme anglais RAM (Random
Access Memory), est la mémoire informatique dans laquelle peuvent être
enregistrées les informations traitées par un appareil
informatique. On écrit mémoire vive par opposition à la mémoire
mortea.

L'acronyme RAM date de 1965.

Les caractéristiques actuelles de cette mémoire sont : Sa fabrication
à base de circuits intégrés ; L'accès direct à l'informationb par
opposition à un accès séquentiel ; Sa rapidité d'accès, essentielle
pour fournir rapidement les données au processeur ; Sa volatilité, qui
entraîne une perte de toutes les données en mémoire dès qu'elle cesse
d'être alimentée en électricité.


Il y a deux types principaux de mémoire vive : La mémoire vive
    dynamique (DRAM) qui, même sous alimentation électrique normale,
    doit être réactualisée périodiquement pour éviter la perte
    d'information ; La mémoire vive statique (SRAM) qui n'a pas besoin
    d'un tel processus sous alimentation électrique normale ;


La mémoire informatique est un composant, d'abord réalisé par une technologie magnétique (tores de ferrite), puis par l'électronique dans les années 1970, qui permet de stocker et relire rapidement des informations binaires. Son rôle est notamment de stocker les données qui vont être traitées par l'unité centrale de traitement (UCT), soit un microprocesseur dans la plupart des appareils modernes.

On peut accéder à la mémoire vive alternativement en lecture ou en écriture.

Il existe également des mémoires associatives, largement utilisées dans les techniques de mémoire virtuelle pour éviter des recherches séquentielles de pages et accélérer ainsi les accès.


Les informations peuvent être organisées en mots de 8, 16, 32 ou 64 bits.

Certaines machines anciennes avaient des mots de taille plus exotique. Par exemple,
60 bits pour le Control Data 6600 ;
36 bits pour l'IBM 7030 « Stretch » ou le DEC PDP-10 ;
12 bits pour la plupart des premiers mini-ordinateurs de DEC, les appareils d'instrumentation travaillant au mieux sur 12 bits à l'époque.

Afin d'assurer la fiabilité de l'information enregistrée en mémoire, on ajoute des bits supplémentaires à chaque mot de mémoire. Par exemple,

- Dans les mémoires à parité, il y a un bit supplémentaire (dit de contrôle de parité), transparent à l'utilisateur (traitement matériel) ;

- Dans les mémoires à correction automatique d'erreur sur 1 bit et détection sur plus d'un bit (ECC), ces bits invisibles sont parfois au nombre de six ou plus ;

- Chaque mot des mémoires des serveurs modernes dits non-stop ou 24×365 dispose, en plus des bits de correction, de bits de remplacement qui prennent la relève des bits défaillants à mesure du vieillissement de la mémoire (une défaillance de 10-11 chaque année se traduit par 10,0 bits défaillants par an sur une mémoire de 128 Gio).

Les fabricants recommandent d'utiliser de barrettes de mémoire avec l'ECC pour celles ayant une capacité d'1 Gio ou plus, en particulier celles utilisées dans les serveurs, permettant de détecter les erreurs et de les corriger à la volée. Dans la pratique, les ordinateurs personnels les utilisent très rarement.

""", "ram.png"),

    Article("Promotion", "13 août 2022", """Nouvelle promotion sur le site!
Entrez le code WHOOPER22 pour profiter d'un rabais de 22%!
""", "discount.png"),

    Article("Le Lorem Ipsum du jour", "13 août 2022", """Est ipsa odit fugit officia ipsum impedit nobis. Ut nemo atque praesentium ea est perferendis. Veniam aut qui labore nihil. Placeat odio aliquam animi labore exercitationem.

Qui minima tenetur consectetur ipsa magni quia autem ab. Nemo sint maiores sapiente porro eum cum. Excepturi qui natus aut. Velit voluptate autem sapiente labore. Molestias quo fuga sed id. Quasi enim consectetur est.

Excepturi ea voluptatum quis autem ea est ea. Iure impedit sequi eligendi dolores. Alias sit laudantium et nostrum iste tempora. Ullam dolorum molestias est iure vel.

Qui temporibus et aliquam et modi saepe et. Nostrum sed magnam alias ipsa qui accusantium hic alias. Ipsum repellendus ullam autem. Repudiandae quos id quo id est aut. Ea ex dolorem necessitatibus in.

Ab sequi molestiae laborum quasi dicta delectus animi qui. Minus repellendus odit est non. Qui fugit excepturi illum itaque in enim rerum. Enim commodi pariatur et similique quibusdam quas. Explicabo aliquid cupiditate ad.

Voluptates nam itaque tempore cum. Quia amet laboriosam error expedita rem vel consectetur. Voluptatem enim earum beatae modi error et itaque. Quibusdam autem molestias inventore. Deserunt est voluptates voluptatum rem eum et eaque. Repellat velit autem deserunt quisquam adipisci ut omnis modi.

Dolor quasi eius quae aut ratione nostrum ratione porro. Ut omnis facilis blanditiis beatae eligendi fugit. Deleniti consequatur ut voluptatem. Ea deleniti sunt quis.

Dolor quasi sit atque explicabo impedit. Fuga dolores ex soluta. Corrupti aut ipsa ab aut ipsum veritatis enim aspernatur. Ullam sit sint suscipit cumque est exercitationem.

Ea aut voluptate a ipsum molestiae pariatur. Non ex veniam ea. Culpa est odio vel beatae ut.

Autem dignissimos esse mollitia eius voluptatem sit cum. Vero alias temporibus blanditiis optio maiores voluptatem natus provident. Repudiandae sint amet officia nesciunt. Reiciendis eligendi sed veniam repudiandae odit accusantium. Aut nobis quia quia dolorem animi perferendis.""", "question.png"),


    Article("Promotion", "18 août 2022", """Nouvelle promotion sur le site!
Entrez le code BLOG25 pour profiter d'un rabais de 25%!
""", "discount.png"),

    Article("Le Lorem Ipsum du jour", "13 août 2022", """Est ipsa odit fugit officia ipsum impedit nobis. Ut nemo atque praesentium ea est perferendis. Veniam aut qui labore nihil. Placeat odio aliquam animi labore exercitationem.

Qui minima tenetur consectetur ipsa magni quia autem ab. Nemo sint maiores sapiente porro eum cum. Excepturi qui natus aut. Velit voluptate autem sapiente labore. Molestias quo fuga sed id. Quasi enim consectetur est.

Excepturi ea voluptatum quis autem ea est ea. Iure impedit sequi eligendi dolores. Alias sit laudantium et nostrum iste tempora. Ullam dolorum molestias est iure vel.

Qui temporibus et aliquam et modi saepe et. Nostrum sed magnam alias ipsa qui accusantium hic alias. Ipsum repellendus ullam autem. Repudiandae quos id quo id est aut. Ea ex dolorem necessitatibus in.

Ab sequi molestiae laborum quasi dicta delectus animi qui. Minus repellendus odit est non. Qui fugit excepturi illum itaque in enim rerum. Enim commodi pariatur et similique quibusdam quas. Explicabo aliquid cupiditate ad.

Voluptates nam itaque tempore cum. Quia amet laboriosam error expedita rem vel consectetur. Voluptatem enim earum beatae modi error et itaque. Quibusdam autem molestias inventore. Deserunt est voluptates voluptatum rem eum et eaque. Repellat velit autem deserunt quisquam adipisci ut omnis modi.

Dolor quasi eius quae aut ratione nostrum ratione porro. Ut omnis facilis blanditiis beatae eligendi fugit. Deleniti consequatur ut voluptatem. Ea deleniti sunt quis.

Dolor quasi sit atque explicabo impedit. Fuga dolores ex soluta. Corrupti aut ipsa ab aut ipsum veritatis enim aspernatur. Ullam sit sint suscipit cumque est exercitationem.

Ea aut voluptate a ipsum molestiae pariatur. Non ex veniam ea. Culpa est odio vel beatae ut.

Autem dignissimos esse mollitia eius voluptatem sit cum. Vero alias temporibus blanditiis optio maiores voluptatem natus provident. Repudiandae sint amet officia nesciunt. Reiciendis eligendi sed veniam repudiandae odit accusantium. Aut nobis quia quia dolorem animi perferendis.""", "question.png"),


    Article("Promotion", "18 août 2022", """Nouvelle promotion sur le site!
Entrez le code LATIN20 pour profiter d'un rabais de 20%!
""", "discount.png"),

    Article("Tout savoir sur les souris", "18 août 2022", """Non nihil quasi odit aut aut voluptatibus id. Mollitia consequatur eos excepturi provident doloremque fugit. Dolorem nisi est cum possimus. Aut quasi rerum necessitatibus. Corrupti aut quidem facilis omnis labore atque. Temporibus rerum doloremque sed et expedita.

Commodi voluptatem consequatur ea. Et ad maxime molestiae rerum. Repudiandae et reprehenderit a placeat velit officia hic voluptatem.

Explicabo iste maiores repudiandae dolorem. Facilis dolore aperiam sequi impedit praesentium est. Accusamus tenetur velit quam quo quas nisi. Earum facilis enim ipsum excepturi. In in odio ipsum nisi dolor aperiam.

Assumenda vitae animi deleniti accusantium. Excepturi dolore sequi odit. Corrupti aut pariatur dolorem nesciunt consequatur quae animi. Ut distinctio repudiandae quia. Assumenda distinctio dolor non quia aliquid voluptatem. Dolorem dicta minus inventore id quasi.

Ullam non modi accusamus repellat numquam dolorem. Eos a culpa corrupti ad ipsam excepturi numquam. Voluptatem quis assumenda voluptatem eveniet cum error omnis. Accusantium blanditiis et sint sint velit sint expedita. Animi aliquid natus odit non non voluptatem neque reprehenderit. Amet et eum rerum non modi cum.

""", "mouse.png"),


]



choix_composantes = {
    'case': [
        Composante(
            'DeepCool MACUBE 110 Micro ATX Case',
            79.99, 'https://www.newegg.ca/p/N82E16811853088'),
        Composante(
            'KEDIERS 7 PCS RGB Fans ATX Mid-Tower PC Gaming Case',
            209.99, 'https://www.newegg.ca/p/2AM-00HH-00036'),
        Composante(
            'LIAN LI O11 Dynamic XL',
            299.99, 'https://www.newegg.ca/p/2AM-000Z-00052'),
    ],
    'motherboard': [
        Composante(
            'GIGABYTE B450M DS3H WIFI AM4 AMD B450 SATA 6Gb/s Micro ATX AMD Motherboard',
            119.99, 'https://www.newegg.ca/p/N82E16813145164'),
        Composante(
            'GIGABYTE B550 GAMING X V2 AM4 AMD B550 SATA 6Gb/s ATX AMD Motherboard',
            199.99, 'https://www.newegg.ca/p/N82E16813145255'),
    ],
    'cpu': [
        Composante(
            'AMD Ryzen 5 5500 - Ryzen 5 5000 Series 6-Core Socket AM4 65W Desktop Processor - 100-100000457BOX',
            179.99, 'https://www.newegg.ca/p/N82E16819113737'),
        Composante(
            'AMD Ryzen 7 5800X - Ryzen 7 5000 Series Vermeer (Zen 3) 8-Core 3.8 GHz Socket AM4 105W Desktop Processor - 100-100000063WOF',
            399.99, 'https://www.newegg.ca/p/N82E16819113665'),
        Composante(
            'AMD Ryzen 9 5900X - Ryzen 9 5000 Series Vermeer (Zen 3) 12-Core 3.7 GHz Socket AM4 105W Desktop Processor - 100-100000061WOF',
            509.99, 'https://www.newegg.ca/p/N82E16819113664'),
        Composante(
            'AMD Ryzen 9 5950X - Ryzen 9 5000 Series Vermeer (Zen 3) 16-Core 3.4 GHz Socket AM4 105W Desktop Processor - 100-100000059WOF',
            699.99, 'https://www.newegg.ca/p/N82E16819113663'),
    ],
    'storage': [
        Composante(
            'Acer SA100 2.5" 960GB SATA Internal Solid State Drive (SSD) BL.9BWWA.104',
            152.99, 'https://www.newegg.ca/p/N82E16820247141'),
        Composante(
            'Reletech P400 Pro Q 2TB NVMe PCIe 4.0 M.2 2280 Internal SSD Maximum Performance Solid State Drive R/W 5000/3700 MB/s Gaming PCI-E Gen 4X4 NVMe(RT-P400Q-2TB)',
            229.90, 'https://www.newegg.ca/p/0D9-00RD-00001'),
        Composante(
            'SAMSUNG 870 QVO Series 2.5" 8TB SATA III Samsung 4-bit MLC V-NAND Internal Solid State Drive (SSD) MZ-77Q8T0B/AM',
            899.99, 'https://www.newegg.ca/p/N82E16820147784'),
    ],
    'cooling': [
        Composante(
            'MasterLiquid ML280 Mirror ARGB Close-Loop AIO CPU Liquid Cooler, Mirror ARGB Pump, 280 Radiator, Dual SickleFlow 140mm, 3rd Gen Dual Chamber Pump for AMD Ryzen/Intel 1200, 1151, LGA 1700 Compatible',
            89.99, 'https://www.newegg.ca/p/N82E16835103312'),
        Composante(
            'Rosewill PB360-RGB RGB CPU Liquid Cooler, Closed Loop PC Water Cooling, Quiet Three 120mm RGB Fans, Connect to the RGB hub which is supporting additional RGB Fans expansion with RGB Synchronization',
            139.99, 'https://www.newegg.ca/p/N82E16835200129'),
        Composante(
            'Lian Li UNI Fan SL120 6 Pack White-with Controller and Extension (ARGB 120mm LED PWM Daisy-Chain) UF-SL120-6W PC Cooling Computer ARGB Case Fans Heatsink Cooler',
            279.99, 'https://www.newegg.ca/p/1YF-01D7-00003'),
    ],
    'ram': [
        Composante(
            'Silicon Power 16GB (2 x 8GB) 288-Pin PC RAM DDR4 2666 (PC4 21300) Desktop Memory Model SU016GBLFU266BD2J5',
            73.99, 'https://www.newegg.ca/p/N82E16820301457'),
        Composante(
            'Samsung 16GB(2X8GB) DDR4 2133MHz PC4-17000 PC4-2133P UDIMM Desktop RAM PC Memory 2Rx8 288 pin M378A1G43DBO-CPB',
            139.92, 'https://www.newegg.ca/p/0RN-00JT-000D7'),
    ],
    'power': [
        Composante(
            'EVGA 500 W3, 80+ 500W, Compact 140mm Size, Non-Modular Active PFC Power Supply, 3 Year Warranty, 100-W3-0500-K1',
            95.99, 'https://www.newegg.ca/p/N82E16817438193'),
        Composante(
            'CORSAIR RM RM750 750 W ATX 80 PLUS GOLD Certified Full Modular Power Supply',
            139.99, 'https://www.newegg.ca/p/N82E16817139280'),
    ],
    'keyboard': [
        Composante(
            'MK1 PC Mechanical Gaming Keyboards - 7-Color LED Backlit Mechanical Keyboard - USB Mechanical Computer Keyboard Wired Blue Switches for MAC/PC Gamers (Black)',
            29.99, 'https://www.newegg.ca/p/32N-00EG-00002'),
        Composante(
            'Corsair CH-9226765-NA K55 RGB PRO Gaming Keyboard',
            88.96, 'https://www.newegg.ca/p/N82E16823816143'),
        Composante(
            'Gamdias Hermes M5 Mechanical Gaming Keyboard with Blue Switches',
            116.90, 'https://www.newegg.ca/p/32N-00CB-00023'),
    ],
    'mouse': [
        Composante(
            'TROPRO RGB Gaming Mouse, 6400 dpi, Ergonomic Hand Grips, RGB Backlit Optical Wired Gaming Mouse 7 Programmable Buttons',
            32.99, 'https://www.newegg.ca/p/32K-00MC-00003'),
        Composante(
            'Corsair Dark Core RGB Pro SE, Wireless FPS/MOBA Gaming Mouse with Slipstream Technology, Black, Backlit RGB LED, 18000 DPI, Optical, Qi Wireless Charging Certified',
            102.48, 'https://www.newegg.ca/p/N82E16826816162'),
        Composante(
            'Logitech PRO X 910-005878 Black 5 Buttons 1 x Wheel Lightspeed Wireless Optical 25400 dpi SUPERLIGHT Gaming Mouse',
            179.99, 'https://www.newegg.ca/p/N82E16826197421')
    ],
    'monitor': [
        Composante(
            'MSI Optix G27C6 27" Full HD 1920 x 1080 165 Hz 2 x HDMI, DisplayPort FreeSync Curved Gaming Monitor',
            312.99, 'https://www.newegg.ca/p/N82E16824475115'),
        Composante(
            'GIGABYTE G34WQC A-SA 34" 144Hz Curved Gaming Monitor, 3440 x 1440 VA 1500R Display, 1ms (MPRT), 90% DCI-P3, VESA Display HDR400, FreeSync Premium, 2x DisplayPort 1.4, 2x HDMI 2.0',
            459.99, 'https://www.newegg.ca/p/N82E16824012046'),
    ]
}
