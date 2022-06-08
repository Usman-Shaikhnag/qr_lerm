# This file is part of lims module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from . import formula_parser
from . import department
from . import configuration
from . import laboratory
from . import analysis
from . import sample
from . import entry
from . import notebook
from . import certification
from . import control_tendency
from . import planification
from . import results_report
from . import stock
from . import uom
from . import party


def register():
    Pool.register(
        formula_parser.FormulaParser,
        department.Department,
        department.UserDepartment,
        configuration.NotebookView,
        configuration.NotebookViewColumn,
        configuration.Printer,
        configuration.User,
        configuration.UserLaboratory,
        configuration.Configuration,
        configuration.ConfigurationLaboratory,
        configuration.ConfigurationSequence,
        configuration.ConfigurationProductCategory,
        configuration.LabWorkYear,
        configuration.LabWorkYearSequence,
        configuration.LabWorkYearHoliday,
        configuration.Cron,
        configuration.ModelDoc,
        configuration.Model,
        laboratory.LaboratoryProfessional,
        laboratory.Laboratory,
        laboratory.LabMethod,
        laboratory.LabMethodWaitingTime,
        laboratory.LabDeviceType,
        laboratory.LabDevice,
        laboratory.LabDeviceLaboratory,
        laboratory.LabDeviceCorrection,
        laboratory.LabDeviceRelateAnalysisStart,
        analysis.ProductType,
        analysis.Matrix,
        analysis.ObjectiveDescription,
        analysis.Formula,
        sample.FractionType,
        laboratory.LaboratoryCVCorrection,
        analysis.FormulaVariable,
        analysis.Analysis,
        analysis.Typification,
        analysis.TypificationAditional,
        analysis.TypificationReadOnly,
        analysis.CalculatedTypification,
        analysis.CalculatedTypificationReadOnly,
        sample.PackagingType,
        analysis.AnalysisIncluded,
        analysis.AnalysisDevice,
        certification.CertificationType,
        certification.TechnicalScope,
        certification.TechnicalScopeVersion,
        certification.TechnicalScopeVersionLine,
        sample.PackagingIntegrity,
        entry.EntrySuspensionReason,
        entry.Entry,
        sample.Zone,
        sample.Variety,
        sample.SampleProducer,
        sample.SampleAttribute,
        sample.Sample,
        sample.Fraction,
        sample.Service,
        uom.ConcentrationLevel,
        entry.EntryDetailAnalysis,
        notebook.Notebook,
        results_report.ResultsReport,
        notebook.NotebookLine,
        notebook.NotebookLineAllFields,
        notebook.NotebookLineProfessional,
        control_tendency.RangeType,
        results_report.ResultsReportVersion,
        results_report.ResultsReportVersionDetail,
        results_report.ResultsReportVersionDetailSample,
        results_report.ResultsReportVersionDetailLine,
        certification.AnalysisFamily,
        certification.AnalysisFamilyCertificant,
        sample.MatrixVariety,
        laboratory.LabDeviceTypeLabMethod,
        laboratory.NotebookRule,
        laboratory.NotebookRuleCondition,
        analysis.AnalysisLaboratory,
        analysis.AnalysisLabMethod,
        notebook.NotebookLineLaboratoryProfessional,
        entry.EntryInvoiceContact,
        entry.EntryReportContact,
        entry.EntryAcknowledgmentContact,
        uom.VolumeConversion,
        uom.UomConversion,
        control_tendency.Range,
        control_tendency.ControlTendency,
        control_tendency.ControlTendencyDetail,
        control_tendency.ControlTendencyDetailRule,
        sample.DuplicateSampleStart,
        sample.DuplicateSampleFromEntryStart,
        analysis.CopyTypificationStart,
        analysis.CopyTypificationConfirm,
        analysis.CopyCalculatedTypificationStart,
        analysis.UpdateTypificationStart,
        analysis.RelateAnalysisStart,
        analysis.OpenAnalysisNotTypifiedStart,
        notebook.NotebookInitialConcentrationCalcStart,
        notebook.NotebookResultsConversionStart,
        notebook.NotebookLimitsValidationStart,
        notebook.NotebookInternalRelationsCalc1Start,
        notebook.NotebookInternalRelationsCalc1Relation,
        notebook.NotebookInternalRelationsCalc1Variable,
        notebook.NotebookInternalRelationsCalc2Start,
        notebook.NotebookInternalRelationsCalc2Result,
        notebook.NotebookInternalRelationsCalc2Relation,
        notebook.NotebookInternalRelationsCalc2Variable,
        notebook.NotebookInternalRelationsCalc2Process,
        notebook.NotebookLoadResultsFormulaStart,
        notebook.NotebookLoadResultsFormulaEmpty,
        notebook.NotebookLoadResultsFormulaResult,
        notebook.NotebookLoadResultsFormulaLine,
        notebook.NotebookLoadResultsFormulaAction,
        notebook.NotebookLoadResultsFormulaProcess,
        notebook.NotebookLoadResultsFormulaVariable,
        notebook.NotebookLoadResultsFormulaBeginning,
        notebook.NotebookLoadResultsFormulaConfirm,
        notebook.NotebookLoadResultsFormulaSit1,
        notebook.NotebookLoadResultsFormulaSit2,
        notebook.NotebookLoadResultsFormulaSit2Detail,
        notebook.NotebookLoadResultsFormulaSit2DetailLine,
        notebook.NotebookLoadResultsManualStart,
        notebook.NotebookLoadResultsManualEmpty,
        notebook.NotebookLoadResultsManualResult,
        notebook.NotebookLoadResultsManualLine,
        notebook.NotebookLoadResultsManualSit1,
        notebook.NotebookLoadResultsManualSit2,
        notebook.NotebookAddInternalRelationsStart,
        notebook.NotebookAcceptLinesStart,
        notebook.NotebookLineRepeatAnalysisStart,
        sample.FractionsByLocationsStart,
        notebook.NotebookResultsVerificationStart,
        notebook.UncertaintyCalcStart,
        notebook.NotebookPrecisionControlStart,
        notebook.NotebookEvaluateRulesStart,
        control_tendency.MeansDeviationsCalcStart,
        control_tendency.MeansDeviationsCalcEmpty,
        control_tendency.MeansDeviationsCalcResult,
        control_tendency.ControlResultLine,
        control_tendency.ControlResultLineDetail,
        control_tendency.MeansDeviationsCalcResult2,
        control_tendency.TendenciesAnalysisStart,
        control_tendency.TendenciesAnalysisResult,
        control_tendency.TrendChart,
        control_tendency.TrendChartAnalysis,
        control_tendency.TrendChartAnalysis2,
        control_tendency.OpenTrendChartStart,
        control_tendency.TrendChartData,
        results_report.DivideReportsResult,
        results_report.DivideReportsDetail,
        results_report.DivideReportsProcess,
        results_report.GenerateResultsReportStart,
        results_report.GenerateResultsReportEmpty,
        results_report.GenerateResultsReportResultAut,
        results_report.GenerateResultsReportResultAutNotebook,
        results_report.GenerateResultsReportResultAutNotebookLine,
        results_report.GenerateResultsReportResultAutExcludedNotebook,
        results_report.GenerateResultsReportResultAutExcludedNotebookLine,
        results_report.GenerateResultsReportResultMan,
        results_report.OpenSamplesPendingReportingStart,
        results_report.GenerateReportStart,
        certification.DuplicateAnalysisFamilyStart,
        results_report.ResultsReportAnnulationStart,
        results_report.NewResultsReportVersionStart,
        sample.CountersampleStorageStart,
        sample.CountersampleStorageEmpty,
        sample.CountersampleStorageResult,
        sample.CountersampleStorageRevertStart,
        sample.CountersampleStorageRevertEmpty,
        sample.CountersampleStorageRevertResult,
        sample.CountersampleDischargeStart,
        sample.CountersampleDischargeEmpty,
        sample.CountersampleDischargeResult,
        sample.FractionDischargeStart,
        sample.FractionDischargeEmpty,
        sample.FractionDischargeResult,
        sample.FractionDischargeRevertStart,
        sample.FractionDischargeRevertEmpty,
        sample.FractionDischargeRevertResult,
        sample.CreateSampleStart,
        sample.CreateSampleService,
        sample.EditSampleServiceStart,
        sample.Referral,
        sample.ReferServiceStart,
        entry.ChangeInvoicePartyStart,
        entry.ChangeInvoicePartyError,
        analysis.AddTypificationsStart,
        analysis.RemoveTypificationsStart,
        notebook.ChangeEstimatedDaysForResultsStart,
        sample.CountersampleStoragePrintStart,
        sample.CountersampleDischargePrintStart,
        notebook.PrintAnalysisPendingInformStart,
        stock.Location,
        stock.Move,
        stock.ShipmentInternal,
        uom.Uom,
        uom.UomCategory,
        uom.Template,
        party.Party,
        party.Address,
        party.Company,
        notebook.PrintAnalysisCheckedPendingInformStart,
        planification.Planification,
        planification.PlanificationTechnician,
        planification.PlanificationTechnicianDetail,
        planification.PlanificationDetail,
        planification.PlanificationServiceDetail,
        planification.NotebookLineFraction,
        planification.PlanificationServiceDetailLaboratoryProfessional,
        planification.PlanificationAnalysis,
        planification.PlanificationFraction,
        planification.FractionReagent,
        planification.LabProfessionalMethod,
        planification.LabProfessionalMethodRequalification,
        planification.LabProfessionalMethodRequalificationSupervisor,
        planification.LabProfessionalMethodRequalificationControl,
        planification.BlindSample,
        planification.RelateTechniciansStart,
        planification.RelateTechniciansResult,
        planification.RelateTechniciansDetail1,
        planification.RelateTechniciansDetail2,
        planification.RelateTechniciansDetail3,
        planification.UnlinkTechniciansStart,
        planification.UnlinkTechniciansDetail1,
        planification.AddFractionControlStart,
        planification.AddFractionRMBMZStart,
        planification.AddFractionBREStart,
        planification.AddFractionMRTStart,
        planification.RemoveControlStart,
        planification.AddAnalysisStart,
        planification.SearchFractionsNext,
        planification.SearchFractionsDetail,
        planification.SearchPlannedFractionsStart,
        planification.SearchPlannedFractionsNext,
        planification.CreateFractionControlStart,
        planification.ReleaseFractionStart,
        planification.ReleaseFractionEmpty,
        planification.ReleaseFractionResult,
        planification.QualificationSituations,
        planification.QualificationSituation,
        planification.QualificationAction,
        planification.QualificationSituation2,
        planification.QualificationSituation3,
        planification.QualificationSituation4,
        planification.ReplaceTechnicianStart,
        planification.PrintBlindSampleReportStart,
        planification.PrintPendingServicesUnplannedReportStart,
        module='lims', type_='model')
    Pool.register(
        entry.PrintAcknowledgmentOfReceipt,
        control_tendency.PrintControlChart,
        sample.CountersampleStoragePrint,
        sample.CountersampleDischargePrint,
        notebook.PrintAnalysisPendingInform,
        sample.DuplicateSample,
        sample.DuplicateSampleFromEntry,
        entry.ForwardAcknowledgmentOfReceipt,
        analysis.CopyTypification,
        analysis.CopyCalculatedTypification,
        analysis.UpdateTypification,
        analysis.RelateAnalysis,
        analysis.CreateAnalysisProduct,
        analysis.OpenAnalysisNotTypified,
        laboratory.LabDeviceRelateAnalysis,
        sample.ManageServices,
        sample.CompleteServices,
        sample.LoadServices,
        notebook.NotebookInitialConcentrationCalc,
        notebook.NotebookLineInitialConcentrationCalc,
        notebook.NotebookResultsConversion,
        notebook.NotebookLineResultsConversion,
        notebook.NotebookLimitsValidation,
        notebook.NotebookLineLimitsValidation,
        notebook.NotebookInternalRelationsCalc1,
        notebook.NotebookLineInternalRelationsCalc1,
        notebook.NotebookInternalRelationsCalc2,
        notebook.NotebookLineInternalRelationsCalc2,
        notebook.NotebookLoadResultsFormula,
        notebook.NotebookLoadResultsManual,
        notebook.NotebookAddInternalRelations,
        notebook.NotebookAcceptLines,
        notebook.NotebookLineAcceptLines,
        notebook.NotebookLineUnacceptLines,
        notebook.NotebookLineRepeatAnalysis,
        sample.FractionsByLocations,
        notebook.NotebookResultsVerification,
        notebook.NotebookLineResultsVerification,
        notebook.UncertaintyCalc,
        notebook.NotebookLineUncertaintyCalc,
        notebook.NotebookPrecisionControl,
        notebook.NotebookLinePrecisionControl,
        notebook.NotebookEvaluateRules,
        notebook.NotebookLineEvaluateRules,
        control_tendency.MeansDeviationsCalc,
        control_tendency.TendenciesAnalysis,
        control_tendency.OpenTrendChart,
        control_tendency.DownloadTrendChart,
        results_report.ResultsLineRepeatAnalysis,
        results_report.DivideReports,
        results_report.GenerateResultsReport,
        results_report.OpenSamplesPendingReporting,
        results_report.GenerateReport,
        results_report.OpenSampleEntry,
        results_report.PrintResultReport,
        results_report.PrintGlobalResultReport,
        certification.DuplicateAnalysisFamily,
        results_report.ServiceResultsReport,
        results_report.FractionResultsReport,
        results_report.SampleResultsReport,
        results_report.SampleResultsReportInProgress,
        results_report.OpenResultsReportSample,
        results_report.OpenResultsDetailEntry,
        results_report.OpenResultsDetailAttachment,
        results_report.ResultsReportRelease,
        results_report.ResultsReportAnnulation,
        results_report.NewResultsReportVersion,
        sample.CountersampleStorage,
        sample.CountersampleStorageRevert,
        sample.CountersampleDischarge,
        sample.FractionDischarge,
        sample.FractionDischargeRevert,
        sample.CreateSample,
        sample.EditSampleService,
        sample.ReferService,
        notebook.OpenNotebookLines,
        entry.ChangeInvoiceParty,
        analysis.OpenTypifications,
        analysis.AddTypifications,
        analysis.RemoveTypifications,
        notebook.ChangeEstimatedDaysForResults,
        notebook.PrintAnalysisCheckedPendingInform,
        notebook.SampleNotebook,
        planification.RelateTechnicians,
        planification.UnlinkTechnicians,
        planification.AddFractionControl,
        planification.AddFractionRMBMZ,
        planification.AddFractionBRE,
        planification.AddFractionMRT,
        planification.RemoveControl,
        planification.AddAnalysis,
        planification.SearchFractions,
        planification.SearchPlannedFractions,
        planification.CreateFractionControl,
        planification.ReleaseFraction,
        planification.TechniciansQualification,
        planification.ReplaceTechnician,
        planification.PrintBlindSampleReport,
        planification.PrintPendingServicesUnplannedReport,
        module='lims', type_='wizard')
    Pool.register(
        entry.AcknowledgmentOfReceipt,
        entry.EntryDetail,
        entry.EntryLabels,
        control_tendency.ControlChartReport,
        control_tendency.TrendChartReport,
        results_report.ResultReport,
        results_report.ResultReportTranscription,
        results_report.GlobalResultReport,
        sample.CountersampleStorageReport,
        sample.CountersampleDischargeReport,
        sample.ReferralReport,
        notebook.AnalysisPendingInform,
        notebook.AnalysisCheckedPendingInform,
        planification.PlanificationSequenceReport,
        planification.PlanificationWorksheetAnalysisReport,
        planification.PlanificationWorksheetMethodReport,
        planification.PlanificationWorksheetReport,
        planification.PendingServicesUnplannedReport,
        planification.PendingServicesUnplannedSpreadsheet,
        planification.BlindSampleReport,
        planification.PlanificationSequenceAnalysisReport,
        module='lims', type_='report')