# ==================== x86 32 =============================================
# data transfer
X86_GRP_DTRANSFER = [
    # general purpose instructions
    "CMOV",
    "CMOVA",
    "CMOVAE",
    "CMOVB",
    "CMOVBE",
    "CMOVC",
    "CMOVE",
    "CMOVG",
    "CMOVGE",
    "CMOVL",
    "CMOVLE",
    "CMOVNA",
    "CMOVNAE",
    "CMOVNB",
    "CMOVNBE",
    "CMOVNC",
    "CMOVNE",
    "CMOVNG",
    "CMOVNGE",
    "CMOVNL",
    "CMOVNLE",
    "CMOVNO",
    "CMOVNP",
    "CMOVNS",
    "CMOVNZ",
    "CMOVO",
    "CMOVP",
    "CMOVPE",
    "CMOVPO",
    "CMOVS",
    "CMOVZ",
    "BSWAP",
    "XCHG",
    "XADD",
    "CMPXCHG",
    "CMPXCHG8B",
    "POP",
    "POPA",
    "POPAD",
    "PUSH",
    "PUSHA",
    "PUSHAD",
    "CDQ",
    "CDQE",
    "CBW",
    "CWD",
    "CWDE",
    "MOV",
    "MOVD",
    "MOVQ",
    "MOVABS",
    "MOVSX",
    "MOVSXD",
    "MOVZX",
    "MOVZXD",
    # string
    "MOVS",
    "MOVSB",
    "MOVSD",
    "MOVSW",
    "STOS",
    "STOSB",
    "STOSD",
    "STOSW",
    "LODS",
    "LODSB",
    "LODSD",
    "LODSW",
    # segment register
    "LDS",
    "LES",
    "LFS",
    "LGS",
    "LSS",
    # user mode extended
    "XSAVE",
    "XSAVEC",
    "XSAVEOPT",
    "XRSTOR",
    "XGETBV",
    "XSETBV",
    # BMI1, BMI2
    "BEXTR",
    "BLSI",
    "PDEP",
    "PEXT",
    # MMX
    "PACKSSDW",
    "PACKSSWB",
    "PACKUSDW",
    "PACKUSWB",
    "PUNPCKHBW",
    "PUNPCKHDQ",
    "PUNPCKHWD",
    "PUNPCKLBW",
    "PUNPCKLDQ",
    "PUNPCKLWD",
    "EMMS",
    # SSE 64-bit integer
    "PMOVMSKB",
    "PSHUFW",
    # SSE2 128-bit integer
    "MOVDQA",
    "MOVDQU",
    "MOVQ2DQ",
    "MOVDQ2Q",
    "PSHUFLW",
    "PSHUFHW",
    "PSHUFD",
    "PUNPCKLQDQ",
    "PUNPCKHQDQ",
    # SSSE2
    "PSHUFB",
    "PALIGNR",
    # SSE4
    "MOVNTDQA",
    "PBLENDVB",
    "PBLENDW",
    "PINSRB",
    "PINSRD",
    "PINSRQ",
    "PEXTRB",
    "PEXTRW",
    "PEXTRD",
    "PEXTRQ",
    "PMOVSXBW",
    "PMOVZXBW",
    "PMOVSXBD",
    "PMOVZXBD",
    "PMOVSXWD",
    "PMOVZXWD",
    "PMOVSXBQ",
    "PMOVZXBQ",
    "PMOVSXWQ",
    "PMOVZXWQ",
    "PMOVSXDQ",
    "PMOVZXDQ",
    "PACKUSDW",
    "LGDT",
    "SGDT",
    "LLDT",
    "SLDT",
    "LTR",
    "STR",
    "LIDT",
    "SIDT",
    "MOV",
    "LMSW",
    "SMSW",
    "CLTS",
    "LSL",
    "LAR",
    "VERR",
    "VERW",
    # 64-bit
    "CDQE",
    "CQO",
]

X86_GRP_FLOAT_DTRANSFER = [
    # floating point instrutions
    "FLD",
    "FST",
    "FSTP",
    "FILD",
    "FIST",
    "FISTP",
    "FBLD",
    "FBSTP",
    "FXCH",
    "FCMOVB",
    "FCMOVBE",
    "FCMOVE",
    "FCMOVNB",
    "FCMOVNBE",
    "FCMOVNE",
    "FCMOVNU",
    "FCMOVU",
    # floating point load const instructions
    "FLD1",
    "FLDZ",
    "FLDPI",
    "FLDL2E",
    "FLDLN2",
    "FLDL2T",
    "FLDLG2",
    # FPU register related
    "FCLEX",
    "FFREE",
    "FINIT",
    "FLDCW",
    "FLDENV",
    "FNCLEX",
    "FNINIT",
    "FNOP",
    "FNSAVE",
    "FNSTCW",
    "FNSTENV",
    "FNSTSW",
    "FRSTOR",
    "FSAVE",
    "FSTCW",
    "FSTENV",
    "FSTSW",
    # SSE
    "MOVAPS",
    "MOVUPS",
    "MOVHPS",
    "MOVHLPS",
    "MOVLPS",
    "MOVLHPS",
    "MOVMSKPS",
    "MOVSS",
    # SSE2
    "MOVAPD",
    "MOVUPD",
    "MOVHPD",
    "MOVHLPD",
    "MOVLPD",
    "MOVLHPD",
    "MOVMSKPD",
    "MOVSD",
    # SSE Shuffle
    "SHUFPS",
    "UNPCKHPS",
    "UNPCKLPS",
    # SSE2 shuffle
    "SHUFPD",
    "UNPCKHPD",
    "UNPCKLPD",
    # SSE Conversion
    "CVTPI2PS",
    "CVTSI2SS",
    "CVTPS2PI",
    "CVTTPS2PI",
    "CVTSS2SI",
    "CVTTSS2SI",
    # SSE2 Conversion
    "CVTPD2PI",
    "CVTTPD2PI",
    "CVTPI2PD",
    "CVTPD2DQ",
    "CVTTPD2DQ",
    "CVTDQ2PD",
    "CVTPS2PD",
    "CVTPD2PS",
    "CVTSS2SD",
    "CVTSD2SS",
    "CVTSD2SI",
    "CVTTSD2SI",
    "CVTSI2SD",
    "CVTDQ2PS",
    "CVTPS2DQ",
    "CVTTPS2DQ",
    # SSE MXCSR State
    "LDMXCSR",
    "STMXCSR",
    # SSE 64-bit
    "PEXTRW",
    "PINSRW",
    # SSE cache
    "MASKMOVQ",
    "MOVNTQ",
    "MOVNTPS",
    "PREFETCH",
    "SFENCE",
    # SSE3
    "FISTTP",
    "LDDQU",
    "MOVSHDUP",
    "MOVSLDUP",
    "MOVDDUP",
    # SSE4
    "BLENDPD",
    "BLENDPS",
    "BLENDVPD",
    "BLENDVPS",
    "EXTRACTPS",
    "INSERTPS",
    # 16-bit FP
    "VCVTPS2PH",
    "VCVTPS2PH",
    # Vector
    "VALIGN",
    "VBLEND",
    "VCOMPRESS",
    "VEXTRACT",
    "VINSERT",
    "VMOV",
    "VFIXUP",
    "VGET",
    "VEXPAND",
    "VCVT",
    "VPBLEND",
    "VPBROAD",
    "VPCOMPRESS",
    "VPERM" "VPEXPAND" "VPMOV",
    "VPSCATTER",
    "VSCATTER",
    "VSHUF",
]

# - Miscellaneous Instructions:
X86_GRP_MISC = [
    "NOP",
    "UD",
    "UD2",
    "LEA",
    "XLAT",
    "XLATB",
    "CPUID",
    "MOVBE",
    "PREFETCHW",
    "PREFETCHWT1",
    "CLFLUSH",
    "CLFLUSHOPT",
    # SSE2 cache
    "CLFLUSH",
    "LFENCE",
    "MFENCE",
    "MASKMOVDQU",
    "MOVNTPD",
    "MOVNTDQ",
    "MOVNTI",
]

X86_GRP_ARITH = [
    # general purpose binary arithmetic instructions
    "ADCX",
    "ADOX",
    "ADC",
    "ADD",
    "XADD",
    "SUB",
    "SBB",
    "IMUL",
    "MUL",
    "IDIV",
    "DIV",
    "INC",
    "DEC",
    "NEG",
    "CMP",
    # decimal arithmetic instructions
    "DAA",
    "DAS",
    "AAA",
    "AAS",
    "AAM",
    "AAD",
    # flag
    "STC",
    "CLC",
    "CMC",
    "CLD",
    "STD",
    # BMI1, BMI2
    "MULX",
    # MMX
    "PADD",
    "PADDB",
    "PADDW",
    "PADDD",
    "PADDSB",
    "PADDSW",
    "PADDUSB",
    "PADDUSW",
    "PSUB",
    "PSUBB",
    "PSUBW",
    "PSUBD",
    "PSUBSB",
    "PSUBSW",
    "PSUBUSB",
    "PSUBUSW",
    "PMULHW",
    "PMULLW",
    "PMADDWD",
    # SSE 64bit integer
    "PAVGB",
    "PAVGW",
    "PMAXUB",
    "PMAXSB",
    "PMINUB",
    "PMINSB",
    "PMULHUW",
    "PSADBW",
    # SSE 128-bit integer
    "PMULUDQ",
    "PADDQ",
    "PSUBQ",
    # SSSE3
    "PHADDW",
    "PHADDSW",
    "PHADDD",
    "PHSUBW",
    "PHSUBSW",
    "PHSUBD",
    "PABSB",
    "PABSW",
    "PABSD",
    "PABSQ",
    "PMADDUBSW",
    "PMULHRSW",
    "PSIGNB",
    "PSIGNW",
    "PSIGND",
    # SSE4
    "PMULLD",
    "PMULDQ",
    "PMINUW",
    "PMINUD",
    "PMINSB",
    "PMINSD",
    "PMAXUW",
    "PMAXUD",
    "PMAXSB",
    "PMAXSD",
    "ROUNDPS",
    "ROUNDPD",
    "ROUNDSS",
    "ROUNDSD",
    "PMPSADBW",
    # AESNI
    "AESDEC",
    "AESDECLAST",
    "AESENC",
    "AESENCLAST",
    "AESIMC",
    "AESKEYGENASSIST",
    "PCLMULQDQ",
    # SHA1
    "SHA1MSG1",
    "SHA1MSG2",
    "SHA1NEXTE",
    "SHA1RNDS4",
    "SHA256MSG1",
    "SHA256MSG2",
    "SHA256RNDS2",
    "CRC32",
    # BMI1, BMI2
    "BLSMSK",
    "BLSR",
    "CLAC",
    "STAC",
]

X86_GRP_FLOAT_CMP = [
    # floating point compare instructions
    "FCOM",
    "FCOMP",
    "FCOMPP",
    "FUCOM",
    "FUCOMP",
    "FUCOMPP",
    "FICOM",
    "FICOMP",
    "FCOMI",
    "FUCOMI",
    "FCOMIP",
    "FUCOMIP",
    "FTST",
    "FXAM",
    # SSE
    "CMPPS",
    "CMPEQPS",
    "CMPNEQPS",
    "CMPLTPS",
    "CMPNLTPS",
    "CMPSS",
    "CMPEQSS",
    "CMPNEQSS",
    "CMPLTSS",
    "CMPNLTSS",
    "COMISS",
    "UCOMISS",
    "CMPPD",
    "CMPEQPD",
    "CMPNEQPD",
    "CMPLTPD",
    "CMPNLTPD",
    "CMPSD",
    "CMPEQSD",
    "CMPNEQSD",
    "CMPLTSD",
    "CMPNLTSD",
    "COMISD",
    "UCOMISD",
    # vector
    "VPCMP",
]

X86_GRP_FLOAT_ARITH = [
    # - floating point instructions:
    "FADD",
    "FADDP",
    "FIADD",
    "FSUB",
    "FSUBP",
    "FISUB",
    "FSUBR",
    "FSUBRP",
    "FISUBR",
    "FMUL",
    "FMULP",
    "FIMUL",
    "FDIV",
    "FDIVP",
    "FIDIV",
    "FDIVR",
    "FDIVRP",
    "FIDIVR",
    "FPREM",
    "FPREM1",
    "FABS",
    "FCHS",
    "FRNDINT",
    "FSCALE",
    "FSQRT",
    "FXTRACT",
    # floating point transcendental instructions
    "FSIN",
    "FCOS",
    "FSINCOS",
    "FPTAN",
    "FPATAN",
    "F2XM1",
    "FYL2X",
    "FYL2XP1",
    # fpu register related
    "FINCSTP",
    "FDECSTP",
    # SSE
    "ADDPS",
    "ADDSS",
    "SUBPS",
    "SUBSS",
    "MULPS",
    "MULSS",
    "DIVPS",
    "DIVSS",
    "RCPPS",
    "RCPSS",
    "SQRTPS",
    "SQRTSS",
    "RSQRTPS",
    "RSQRTSS",
    "MAXPS",
    "MAXSS",
    "MINPS",
    "MINSS",
    # SSE2
    "ADDSD",
    "SUBSD",
    "MULSD",
    "DIVSD",
    "RCPSD",
    "SQRTSD",
    "RSQRTSD",
    "MAXSD",
    "MINSD",
    # SSE3
    "ADDSUBPS",
    "ADDSUBPD",
    "HADDPS",
    "HSUBPS",
    "HADDPD",
    "HSUBPD",
    # SSE4
    "DPPD",
    "DPPS",
    # vector
    "VPMAX",
    "VPMIN",
    "VRCP",
    "VRNDSCAL",
    "VRSQRT",
    "VSCALE",
    "ADDPD",
    "ADDSD",
    "MULPD",
    "MULSD",
    "SUBPD",
    "SUBSD",
    "DIVPD",
    "DIVSD",
    "RCPPD",
    "RCPSD",
]

X86_GRP_CMP = [
    "CMP",
    "COMI",
    "CLT",
    # from dtransfer
    "CMPXCHG",
    "CMPXCHG8B",
    # from bit
    "TEST",
    # from string
    "CMPS",
    "CMPSB",
    "CMPSD",
    "CMPSW",
    # MMX
    "PCMPEQB",
    "PCMPEQW",
    "PCMPEQD",
    "PCMPGTB",
    "PCMPGTW",
    "PCMPGTD",
    # SSE4
    "PHMINPOSUW",
    "PTEST",
    "PCMPEQQ",
    # SSE4.2
    "PCMPESTRI",
    "PCMPESTRM",
    "PCMPISTRI",
    "PCMPISTRM",
    "PCMPGTQ",
    # Vector
    "VPTEST",
]

# Shift and Rotate Instructions:
X86_GRP_SHIFT = [
    # general purpose instructions
    "SAR",
    "SHR",
    "SAL",
    "SHL",
    "SHRD",
    "SHLD",
    "ROR",
    "ROL",
    "RCR",
    "RCL",
    # BMI1, BMI2
    "RORX",
    "SARX",
    "SHLX",
    "SHRX",
    # MMX
    "PSLLW",
    "PSLLD",
    "PSLLQ",
    "PSRLW",
    "PSRLD",
    "PSRLQ",
    "PSRAW",
    "PSRAD",
    # SSE2 128-bit integer
    "PSLLDQ",
    "PSRLDQ",
    # vector
    "VPROL",
    "VPROR",
    "VPSRA",
    "VPSLL",
    "VPSRA",
]

# Logical Instructions:
X86_GRP_LOGIC = [
    # general purpose instructions
    "AND",
    "NOT",
    "OR",
    "XOR",
    # BMI1, BMI2
    "ANDN",
    # MMX
    "PAND",
    "PANDN",
    "POR",
    "PXOR",
    # SSE
    "ANDPS",
    "ANDNPS",
    "ORPS",
    "XORPS",
    # SSE2
    "ANDPD",
    "ANDNPD",
    "ORPD",
    "XORPD",
    # Vector
    "VPTERLOG",
]

# bit and byte instructions:
X86_GRP_BIT = [
    # general purpose instructions
    "SETA",
    "SETAE",
    "SETB",
    "SETBE",
    "SETC",
    "SETE",
    "SETG",
    "SETGE",
    "SETL",
    "SETLE",
    "SETNA",
    "SETNAE",
    "SETNB",
    "SETNBE",
    "SETNC",
    "SETNE",
    "SETNG",
    "SETNGE",
    "SETNL",
    "SETNLE",
    "SETNO",
    "SETNP",
    "SETNS",
    "SETNZ",
    "SETO",
    "SETP",
    "SETPE",
    "SETPO",
    "SETS",
    "SETZ",
    "TEST",
    "CRC32",
    # BMI1, BMI2
    "BLSMSK",
    "BLSR",
    "CLAC",
    "STAC",
    # from bit
    "TEST",
    "BT",
    "BTS",
    "BTR",
    "BTC",
    "BSF",
    "BSR",
    "POPCNT",
    "TZCNT",
    "LZCNT",
]

# control transfer instructions:
X86_GRP_CTRANSFER = [
    # general purpose instructions
    "JMP",
    "CALL",
    "RET",
    "IRET",
    "INT",
    "INTO",
    "BOUND",
    "ENTER",
    "LEAVE",
    # flag
    "CLI",
    "STI",
    # SSE2
    "PAUSE",
    # SSE3
    "MONITOR",
    "MWAIT",
    "XABORT",
    "XACQUIRE",
    "XRELEASE",
    "XBEGIN",
    "XEND",
    "XTEST",
    "HLT",
    "SYSCALL",
    "SYSENTER",
    "SYSEXIT",
    "SYSRET",
    "FWAIT",
    "WAIT",
    # vm related instructions
    "VMCALL",
    "VMLAUNCH",
    "VMMCALL",
    "VMRESUME",
    "VMRUN",
    "VMFUNC",
    "VMCLEAR",
    "VMXON",
    "VMXOFF",
]

X86_GRP_COND_CTRANSFER = [
    # general purpose instructions
    "JA",
    "JAE",
    "JB",
    "JBE",
    "JC",
    "JCXZ",
    "JE",
    "JECXZ",
    "JRCXZ",
    "JG",
    "JGE",
    "JL",
    "JLE",
    "JNAE",
    "JNB",
    "JNBE",
    "JNC",
    "JNE",
    "JNG",
    "JNGE",
    "JNL",
    "JNLE",
    "JNO",
    "JNP",
    "JNS",
    "JNZ",
    "JO",
    "JP",
    "JPE",
    "JPO",
    "JS",
    "JZ",
    "LOOP",
    "LOOPE",
    "LOOPNE",
    "LOOPNZ",
    "LOOPZ",
    # string
    "REP",
    "REP MOVSQ",
    "REP STOSQ",
    "REPNE",
    "REPNZ",
    "REPE",
    "REPZ",
]

# ==================== ARM 32 =============================================
ARM_GRP_DTRANSFER = [
    # general purpose instructions
    "LDA",
    "ADR",
    "ADRP",
    "LDR",
    "LDRD",
    "LDRB",
    "LDRBT",
    "LDRH",
    "LDRS",
    "LDRSB",
    "LDRSBT",
    "LDRSH",
    "LDRSHT",
    "LDRT",
    "LDRHT",
    "STR",
    "STRB",
    "STRD",
    "STRH",
    "STRBT",
    "STRT",
    "LDM",
    "LDMDA",
    "LDMDB",
    "LDMIB",
    "STM",
    "STMDA",
    "STMDB",
    "STMIB",
    "PLD",
    "SWP",
    "MOV",
    "MOVI",
    "MOVK",
    "MOVZ",
    "MOVT",
    "MOVN",
    "MVN",
    "MVNI",
    "STP",
    "LDP",
    "RFEIB",
    # coprocessor data operations
    "CDP",
    "MCR",
    "MCRR",
    "MRC",
    "MRR",
    "LDC",
    "LDCL",
    "STC",
    "STCL",
    "PUSH",
    "SBFX",
    "SBFIZ",
    "BFX",
    "BFXIL",
    "UBFX",
    "UBFIZ",
    "VLD",
    "VST",
    "VST2",
    "VSTMDB",
    "VTBL",
    "VTBX",
    "ZIP",
    "ZIP1",
    "ZIP2",
    "UZP",
    "UZP1",
    "UZP2",
    "XTN",
    "XTN2",
    "CSEL",
    "LD1",
    "LD2",
    "LD4",
    "ST1",
    "ST2",
    "ST4",
    "LDPSW",
    "LDRSW",
    "SXTAB",
    "SXTB",
    "SXTH",
    "SXTW",
    "EXT",
    "EXTR",
    "INS",
    "UXTAB",
    "UXTB",
    "UXTH",
    "UXTW",
    "BFC",
    "BFI",
    "BIC",
    "CLZ",
    "REV",
    "REV16",
    "REV32",
    "REV64",
    "CSET",
]

ARM_GRP_FLOAT_DTRANSFER = [
    # floating point data transfer instructions
    "FCPY",
    "FCVTMS",
    "FCVTMU",
    "FCVTZS",
    "FCVTZU",
    "FCVT",
    "FLD",
    "FST",
    "FMR",
    "FMD",
    "FMS",
    "FMX",
    "FSITO",
    "FUITO",
    "FTOSI",
    "FTOUI",
    "FMOV",
    "UMOV",
    "LDUR",
    "LDURB",
    "LDURH",
    "LDURSB",
    "LDURSH",
    "LDURSW",
    "STUR",
    "STURB",
    "STURH",
    "STURSB",
    "STURSH",
    "STURSW",
    "DUP",
    "SCVTF",
    "UCVTF",
]

ARM_GRP_MISC = [
    "UDF",
    "NOP",
    "MRS",
    "MSR",
    "MAR",
    "MRA",
    "VMRS",
    "VMSR",
    "DBG",
    "DMB",
    "DSB",
    "ISB",
    "SETEND",
]

# binary arithmetic instructions:
ARM_GRP_ARITH = [
    # general purpose instructions
    "ADD",
    "ADDW",
    "ADDP",
    "ADDV",
    "ADC",
    "SUB",
    "SBC",
    "RSB",
    "RSC",
    "CMN",
    "CLZ",
    "MUL",
    "MLA",
    "MLS",
    "CINC",
    "CINV",
    "NEG",
    "NEGS",
    "DIV",
    "SMAX",
    "SMAXV",
    "SMIN",
    "SMINV",
    "UMULL",
    "UMLAL",
    "UMLAL2",
    "SMLA",
    "SMLAL",
    "SMLALTT",
    "SMUL",
    "SMSUB",
    "MADD",
    "MNEG",
    "MSUB",
    "SMADDL",
    "SMNEGL",
    "SMSUBL",
    "SMULH",
    "SMULL",
    "UMADDL",
    "UMNEGL",
    "UMSUBL",
    "UMULH",
    "UMULL",
    "SDIV",
    "UDIV",
    "MIA",
    "QADD",
    "QSUB",
    "QDADD",
    "QDSUB",
    "QASX",
    "SADD",
    "SADDW",
    "SADDW2",
    "SASX",
    "SHADD",
    "SHASX",
    "SMLSD",
    "SMMLA",
    "SMUAD",
    "SMUSD",
    "SSUB",
    "SAT",
    "SAX",
    "UADD",
    "UADDW",
    "UADDW2",
    "USAT",
    "USAX",
    "UASX",
    "UHADD",
    "UHASX",
    "UMLSD",
    "UMMLA",
    "UQADD",
    "UQSAX",
    "UQSUB",
    "UHSAX",
    "VABA",
    "VABD",
    "MAX",
    "MIN",
    "VMLA",
    "VMLS",
    "VNMUL",
    "VNMLA",
    "VNMLS",
    "VFMS",
    "VFMS",
    "VFMA",
    "VFMS",
    "VFNMA",
    "VFNMS",
    "VRECPE",
    "VSQRT",
    "VQRSH",
    "UMULL",
    "UMAAL",
    "UMLAL",
    "USADA8",
    "VNEG",
    "CNEG",
    "CSINC",
    "CSINV",
    "CSNEG",
]

ARM_GRP_FLOAT_ARITH = [
    # floating point arithmetic instructions
    "FABS",
    "FABD",
    "FADD",
    "FSUB",
    "FDIV",
    "FMUL",
    "FNMUL",
    "FSQRT",
    "FMAC",
    "FNMAC",
    "FMSC",
    "FNMSC",
    "FNEG",
    "FMADD",
    "FMSUB",
    "FNMADD",
    "FNMSUB",
    "FPINT",
    "FCSEL",
    "FMAX",
    "FMIN",
    "FMLA",
    "FMLS",
    "FRINTM",
    "FRINTP",
    "FRINT",
]

ARM_GRP_SHIFT = [
    # shift operations
    "ASR",
    "LSL",
    "LSR",
    "ROR",
    "RRX",
    "PKHBT",
    "PKHTB",
    "SHL",
    "USHL",
    "USHLL",
    "USHLL2",
    "USHR",
    "USRA",
    "SSHL",
    "SSHLL",
    "SSHLL2",
    "SSHR",
]

ARM_GRP_CMP = [
    # compare instructions
    "CMEQ",
    "CMGT",
    "CMHI",
    "CMHS",
    "CMP",
    "CCMN",
    "CCMP",
    "VCEQ",
    "VCGE",
    "VCGT",
    "VCLE",
    "VCLT",
    # from bit
    "TST",
    "TEQ",
]

ARM_GRP_FLOAT_CMP = [
    "VCMP",
    "VCMPE",
    "FCMPE",
    "FCMGT",
    "FCM",
    "FCMP",
    "FCCMP",
    "VCM",
]

# Logical Instructions:
ARM_GRP_LOGIC = [
    "AND",
    "ORR",
    "EOR",
    "EON",
    "ORN",
]

# bit and byte instructions:
ARM_GRP_BIT = [
    "TST",
    "TEQ",
    "BSL",
    "BIF",
    "BIT",
    "BFC",
    "BFI",
    "BIC",
    "CLZ",
    "RBIT",
    "REV",
    "REV16",
    "REV32",
    "REV64",
    "CSET",
]

# control transfer instructions:
ARM_GRP_CTRANSFER = [
    "B",
    "BR",
    "BL",
    "BLR",
    "BX",
    "BLX",
    "BXJ",
    "BAL",
    "BLAL",
    "BXAL",
    "BLXAL",
    "BXJAL",
    "SWI",
    "BKPT",
    "RET",
    "YIELD",
    "WFE",
    "WFI",
    "SEV",
    "SEVL",
    "CPS",
    "BRK",
    "HLT",
    "SVC",
    "HVC",
    "SMC",
    "TRAP",
    "ERET",
    # ARM POP is return
    "POP",
]

ARM_GRP_COND_CTRANSFER = [
    "BEQ",
    "BNE",
    "BCS",
    "BCC",
    "BMI",
    "BPL",
    "BVS",
    "BVC",
    "BHI",
    "BLS",
    "BGE",
    "BLT",
    "BGT",
    "BLE",
    "BLEQ",
    "BLNE",
    "BLCS",
    "BLCC",
    "BLMI",
    "BLPL",
    "BLVS",
    "BLVC",
    "BLHI",
    "BLLS",
    "BLGE",
    "BLLT",
    "BLGT",
    "BLLE",
    "BXEQ",
    "BXNE",
    "BXCS",
    "BXCC",
    "BXMI",
    "BXPL",
    "BXVS",
    "BXVC",
    "BXHI",
    "BXLS",
    "BXGE",
    "BXLT",
    "BXGT",
    "BXLE",
    "BLXEQ",
    "BLXNE",
    "BLXCS",
    "BLXCC",
    "BLXMI",
    "BLXPL",
    "BLXVS",
    "BLXVC",
    "BLXHI",
    "BLXLS",
    "BLXGE",
    "BLXLT",
    "BLXGT",
    "BLXLE",
    "BXJEQ",
    "BXJNE",
    "BXJCS",
    "BXJCC",
    "BXJMI",
    "BXJPL",
    "BXJVS",
    "BXJVC",
    "BXJHI",
    "BXJLS",
    "BXJGE",
    "BXJLT",
    "BXJGT",
    "BXJLE",
    "TBZ",
    "TBNZ",
    # combined instructions
    "CBZ",
    "CBNZ",
]

# ==================== MIPS 32 =============================================
# data transfer
# refernce : https://www.cs.cornell.edu/courses/cs3410/2008fa/MIPS_Vol2.pdf
MIPS_GRP_DTRANSFER = [
    "LB",
    "LBU",
    "LH",
    "LHU",
    "LL",
    "LW",
    "LWU",
    "LD",
    "LDL",
    "LDR",
    "LWL",
    "LWR",
    "PREF",
    "SB",
    "SC",
    "SD",
    "SDL",
    "SDR",
    "SH",
    "ST",
    "SW",
    "SWL",
    "SWR",
    "SYNC",
    "LUI",
    "LDXC1",
    "LWXC1",
    "SDXC1",
    "SWXC1",
    "MFHI",
    "MFLO",
    "MOV",
    "MOVF",
    "MOVN",
    "MOVT",
    "MOVZ",
    "MTHI",
    "MTLO",
    "MOVE",
    "CVT",
    "LDC",
    "LWC",
    "SDC",
    "SWC",
    # move
    "CFC",
    "CTC",
    "MFC",
    "MTC",
    "PREF",
    "SYNC",
    "SPLAT",
    "CFCMSA",
    "CTCMSA",
    "COPY",
    "PUSH",
    "SEH",
    "SEB",
    "WSBH",
    "DSBH",
    "DSHD",
    "MTC0",
    "MFC0",
    "LDC3",
    "LWC3",
    "SDC3",
    "SWC3",
    # coprocessor load, store
    "COP2",
    "LDC2",
    "LWC2",
    "SDC2",
    "SWC2",
    # cop move
    "CFC2",
    "CTC2",
    "MFC2",
    "MTC2",
]

MIPS_GRP_FLOAT_DTRANSFER = [
    # floating point
    "FRINT",
    "FCLASS",
    # load, store, memory
    "LDC1",
    "LWC1",
    "SDC1",
    "SWC1",
    # move
    "CFC1",
    "CTC1",
    "MFC1",
    "FMOV",
    "MOVF",
    "MOVN",
    "MOVT",
    "MOVZ",
    "MTC1",
    # convert
    "FEX",
    "FFINT",
    "FFQ",
    "FTINT",
    "FTRUN",
    "FTQ",
    "FCVT",
    "FLOOR",
    "ROUND",
    "TRUNC",
    "FFLOOR",
    "FROUND",
    "FTRUNC",
    "DMFC",
    "DMFC1",
    "DMTC",
    "DMTC1",
    "MTHC1",
    "MFHC1",
]

# binary arithmetic instructions:
MIPS_GRP_ARITH = [
    # general purpose instructions
    "ADD",
    "ADDI",
    "ADDU",
    "ADDIU",
    "SUB",
    "SUBU",
    "MUL",
    "MULT",
    "MULTU",
    "CLO",
    "CLZ",
    "DIV",
    "DIVU",
    "MADD",
    "MADDU",
    "MSUB",
    "MSUBU",
    "AADD",
    "ASUB",
    "ABS",
    "NEG",
    "NEGU",
    # additional
    "DAA",
    "DSUB",
    "DSUBU",
    "DSUBIU",
    "DDIV",
    "DDIVU",
    "DDIVIU",
    "DMUL",
    "DMULT",
    "DMULTU",
    "DOTP",
    "DPADD",
    "DPSUB",
    "MADD",
    "MAX",
    "MIN",
    "MSUB",
    "MOD",
    "SAT",
    "HSUB",
    "SQRT",
    "AUI",
    "DAUI",
    "DAHI",
    "DATI",
    "ADDIUPC",
    "AUIPC",
    "ALUIPC",
    "DADD",
    "DADDU",
    "DADDIU",
    "DCLZ",
    # from bit
    "BMZ",
    "BMN",
    "BNEG",
]

MIPS_GRP_CMP = [
    "SLT",
    "SLTI",
    "SLTIU",
    "SLTU",
    # compare instructions
    "CMP",
    "CEQ",
    "CLE",
    "CLT",
    "CF",
    "CUN",
    "CEQ",
    "CUEQ",
    "COLT",
    "CULT",
    "COLE",
    "CULE",
    "CSF",
    "CNGLE",
    "CSEQ",
    "CNGL",
    "CLT",
    "CNGE",
    "CLE",
    "CNGT",
    "CMP",
    "CEQ",
    "CLE",
    "CLT",
    "CF",
    "CUN",
    "CEQ",
    "CUEQ",
    "COLT",
    "CULT",
    "COLE",
    "CULE",
    "CSF",
    "CNGLE",
    "CSEQ",
    "CNGL",
    "CLT",
    "CNGE",
    "CLE",
    "CNGT",
    "C",
]

MIPS_GRP_FLOAT_CMP = [
    # floating point compare instructions
    "FACF",
    "FC",
    "FS",
]

MIPS_GRP_SHIFT = [
    # shift operation
    "SLL",
    "SLLV",
    "SRL",
    "SRLV",
    "SRA",
    "SRAV",
    "SHL",
    "SHR",
    "SLD",
    "DSLL",
    "DSLL32",
    "DSLLV",
    "DSRA",
    "DSRA32",
    "DSRAV",
    "DSRL",
    "DSRL32",
    "DSRLV",
    "ROTR",
    "ROTRV",
    "DROTR",
    "DROTR32",
    "DROTRV",
    "LSA",
    "DLSA",
]

MIPS_GRP_FLOAT_ARITH = [
    # floating point
    "FABS",
    "FADD",
    "FDIV",
    "FMADD",
    "FMSUB",
    "FMUL",
    "FNEG",
    "FNMADD",
    "FNMSUB",
    "FEXP",
    "FLOG",
    "FMAX",
    "FMIN",
    "FRCP",
    "RECIP",
    "FRECIP",
    "FRSQRT",
    "FSQRT",
    "FSUB",
]

# Logical Instructions:
MIPS_GRP_LOGIC = [
    "AND",
    "ANDI",
    "NOR",
    "OR",
    "NOT",
    "ORI",
    "XOR",
    "XORI",
]

# bit and byte instructions:
MIPS_GRP_BIT = [
    "BINS",
    "DINS",
    "DEXT",
    "EXT",
    "INS",
    "BMZ",
    "BMN",
    "BNEG",
    "BSEL",
    "BSET",
    "BCLR",
    # bit wise count
    "NLOC",
    "NLZC",
    "PCNT",
]

MIPS_GRP_MISC = [
    "NOP",
    "SSNOP",
    "CACHE",
    "TLBP",
    "TLBR",
    "TLBWI",
    "TLBWR",
]

# control transfer instructions:
MIPS_GRP_CTRANSFER = [
    "B",
    "BAL",
    "J",
    "JAL",
    "JR",
    "JALR",
    "BREAK",
    "SYSCALL",
    "PAUSE",
    "WAIT",
    "HLT",
    "ERET",
    "DERET",
    "SDBBP",
    "BKPT",
    "RET",
    "MFC0",
    "MTC0",
    # MIPS POP is return
    "POP",
    # float
    "BC1",
    "BC1F",
    "BC1T",
    "BC1FL",
    "BC1TL",
    # cop
    "BC2F",
    "BC2T",
    "BC2FL",
    "BC2TL",
    "BC3F",
    "BC3T",
    "BC3FL",
    "BC3TL",
]

MIPS_GRP_COND_CTRANSFER = [
    "BEQ",
    "BEQZ",
    "BNE",
    "BGE",
    "BGEZ",
    "BGEZAL",
    "BGTZ",
    "BLEZ",
    "BLTZ",
    "BLTZAL",
    "BNEL",
    "BNEZ",
    "BNZ",
    "TEQ",
    "TEQI",
    "TGE",
    "TGEI",
    "TGEIU",
    "TGEU",
    "TLT",
    "TLTI",
    "TLTIU",
    "TLTU",
    "TNE",
    "TNEI",
    "BEQL",
    "BGEZALL",
    "BGEZL",
    "BGTZL",
    "BLEZL",
    "BLTZALL",
    "BLTZL",
    "BNEL",
]

# ============================================
# Below part creates dictionary which groups instructions
X86_GRP_MAP = {
    9: X86_GRP_FLOAT_DTRANSFER + X86_GRP_FLOAT_CMP + X86_GRP_FLOAT_ARITH,
    10: X86_GRP_MISC + X86_GRP_FLOAT_DTRANSFER + X86_GRP_DTRANSFER,
    11: X86_GRP_FLOAT_ARITH + X86_GRP_SHIFT + X86_GRP_ARITH,
    12: X86_GRP_LOGIC,
    13: X86_GRP_COND_CTRANSFER + X86_GRP_CTRANSFER,
    20: X86_GRP_FLOAT_DTRANSFER + X86_GRP_DTRANSFER,
    21: X86_GRP_FLOAT_ARITH + X86_GRP_ARITH,
    22: X86_GRP_FLOAT_CMP + X86_GRP_CMP,
    23: X86_GRP_SHIFT,
    24: X86_GRP_BIT,
    26: X86_GRP_COND_CTRANSFER,
    27: X86_GRP_CTRANSFER,
    28: X86_GRP_MISC,
    30: [],
}

ARM_GRP_MAP = {
    9: ARM_GRP_FLOAT_DTRANSFER + ARM_GRP_FLOAT_CMP + ARM_GRP_FLOAT_ARITH,
    10: ARM_GRP_MISC + ARM_GRP_FLOAT_DTRANSFER + ARM_GRP_DTRANSFER,
    11: ARM_GRP_FLOAT_ARITH + ARM_GRP_SHIFT + ARM_GRP_ARITH,
    12: ARM_GRP_LOGIC,
    13: ARM_GRP_COND_CTRANSFER + ARM_GRP_CTRANSFER,
    20: ARM_GRP_FLOAT_DTRANSFER + ARM_GRP_DTRANSFER,
    21: ARM_GRP_FLOAT_ARITH + ARM_GRP_ARITH,
    22: ARM_GRP_FLOAT_CMP + ARM_GRP_CMP,
    23: ARM_GRP_SHIFT,
    24: ARM_GRP_BIT,
    26: ARM_GRP_COND_CTRANSFER,
    27: ARM_GRP_CTRANSFER,
    28: ARM_GRP_MISC,
    30: [],
}

# A64 does not allow instructions to be conditionally executed as ARM.
def _copy_for_arm64():
    import copy

    return copy.deepcopy(ARM_GRP_MAP)


ARM64_GRP_MAP = _copy_for_arm64()

# ARM instructions may have conditional suffix. Thus, initialize here. However,
# reference : http://infocenter.arm.com/help/index.jsp
ARM_COND_GROUPS = [9, 10, 11, 13, 20, 21, 22, 26]
ARM_GRP_COND_CODE = [
    "EQ",
    "NE",
    "CS",
    "HS",
    "CC",
    "LO",
    "MI",
    "PL",
    "VS",
    "VC",
    "HI",
    "LS",
    "GE",
    "LT",
    "GT",
    "LE",
    "AL",
]
# for group_no in ARM_COND_GROUPS:
#    for inst in ARM_GRP_MAP[group_no]:
#        for cond in ARM_GRP_COND_CODE:
#            ARM_GRP_MAP[group_no].append(inst + cond)

MIPS_GRP_MAP = {
    9: MIPS_GRP_FLOAT_DTRANSFER + MIPS_GRP_FLOAT_CMP + MIPS_GRP_FLOAT_ARITH,
    10: MIPS_GRP_MISC + MIPS_GRP_FLOAT_DTRANSFER + MIPS_GRP_DTRANSFER,
    11: MIPS_GRP_FLOAT_ARITH + MIPS_GRP_SHIFT + MIPS_GRP_ARITH,
    12: MIPS_GRP_LOGIC,
    13: MIPS_GRP_COND_CTRANSFER + MIPS_GRP_CTRANSFER,
    20: MIPS_GRP_FLOAT_DTRANSFER + MIPS_GRP_DTRANSFER,
    21: MIPS_GRP_FLOAT_ARITH + MIPS_GRP_ARITH,
    # mips usually contains compare in conditional branch
    22: MIPS_GRP_FLOAT_CMP + MIPS_GRP_CMP + MIPS_GRP_COND_CTRANSFER,
    23: MIPS_GRP_SHIFT,
    24: MIPS_GRP_BIT,
    26: MIPS_GRP_COND_CTRANSFER,
    27: MIPS_GRP_CTRANSFER,
    28: MIPS_GRP_MISC,
    30: [],
}

# ============================================
GRP_NO_MAP = {
    # Among capstone's default mapping, use 1, 2, 3 as they are common in all
    # architectures.
    1: "grp_jump",
    2: "grp_call",
    3: "grp_ret",
    9: "floatinst",
    10: "abs_dtransfer",
    11: "abs_arith",
    12: "logic",
    13: "abs_ctransfer",
    20: "dtransfer",
    21: "arith",
    22: "cmp",
    23: "shift",
    24: "bitflag",
    26: "cndctransfer",
    27: "ctransfer",
    28: "misc",
    30: "unknown",
}
GRP_NAME_MAP = {val: key for key, val in GRP_NO_MAP.items()}

# ============================================
# Below part maps capstone's internal instruction numbers to pre-defined groups
def _check_inst(target_inst, check_list, suffixes=[]):
    target_inst = target_inst.split("_")[0]
    target_inst = target_inst.split(".")[0]
    target_inst = target_inst.upper()
    for inst in check_list:
        if target_inst == inst:
            return True
        # Check conditional code
        if target_inst.startswith(inst):
            if len(target_inst) - len(inst) == 2:
                for suffix in suffixes:
                    if target_inst == inst + suffix:
                        return True
    return False


def _init_inst_groups(prefix, target, groups):
    insts = list(filter(lambda x: x.startswith(prefix), dir(target)))
    inst_map = {}
    if prefix == "ARM_INS_":
        suffixes = ARM_GRP_COND_CODE
    else:
        suffixes = []
    for inst in insts:
        inst_no = getattr(target, inst)
        inst = inst.replace(prefix, "")
        inst_map[inst_no] = []
        for group_no, grouped_insts in groups.items():
            if _check_inst(inst, grouped_insts, suffixes):
                inst_map[inst_no].append(group_no)

        if not inst_map[inst_no]:
            inst_map[inst_no].append(GRP_NAME_MAP["unknown"])

    return inst_map


def _init_groups():
    import capstone

    x86 = _init_inst_groups("X86_INS_", capstone.x86, X86_GRP_MAP)
    arm = _init_inst_groups("ARM_INS_", capstone.arm, ARM_GRP_MAP)
    arm64 = _init_inst_groups("ARM64_INS_", capstone.arm64, ARM64_GRP_MAP)
    mips = _init_inst_groups("MIPS_INS_", capstone.mips, MIPS_GRP_MAP)
    return x86, arm, arm64, mips


X86_INST_MAP, ARM_INST_MAP, ARM64_INST_MAP, MIPS_INST_MAP = _init_groups()